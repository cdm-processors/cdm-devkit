from functools import reduce

from colorama import Fore

from .parser import parse
from .synth import epilog, preamble, synth
from .util import log2
from .args import args


def main():
    fname = args.defs
    if fname.endswith('.def'):
        fname = fname[:-4]

    with open(fname + '.def') as fd:
        rules, seqwidth, phases, triggers = parse(fd.read())

    def hasreps(x):
        if not x:
            return ""
        if x[0] not in x[1:]:
            return hasreps(x[1:])
        else:
            return x[0]

    def err(msg):
        if args.color:
            print(Fore.RED + msg + Fore.RESET)
        else:
            print(msg)

        quit(-1)

    def print_colored(msg, color: Fore):
        if args.color:
            print(color + msg + Fore.RESET)
        else:
            print(msg)

    repeated = hasreps(triggers)
    if repeated:
        err("Trigger '" + repeated + "' occurs more than once on trigger list")

    triggers.sort()
    triggers.append('CUT')

    opcodes = [op for (op, _) in rules]

    repeated = hasreps(opcodes)
    if repeated:
        err("Opcode '" + repeated + "' occurs more than once on activation list")

    trval = {}
    v = 1
    for tr in triggers:
        trval[tr] = v
        v = 2 * v

    print_colored("*** SECONDARY DECODER SYNTH ***", Fore.BLUE)

    print("\tSequencer width: " + str(seqwidth))
    print("\tMaximum phases per instruction: " + str(phases))
    print("\tTrigger list:")
    print('\t\t' + (', \n\t\t'.join(["%s(0x%X)" % (tr, trval[tr]) for tr in triggers])))
    print("\nProcessing action lists...")

    fill_value = 0
    try:
        fill_value = int(args.fill, 16)
    except ValueError:
        err(f"Invalid fill value: {args.fill}, expected hex number")

    content = [[] for _ in range(phases)]  # can't use phases*[[]], idiotic Python will create refs to same obj.

    for rule in rules:
        opc, optrigs = rule

        if len(optrigs) > phases:
            err(str(len(optrigs)) + " phases specified for opcode '" + opc + "', greater than maximum declared")

        for phno in range(phases):
            if args.debug and phno == 0:
                print('\t' + opc + ': ' + '; '.join([', '.join(p) for p in optrigs]))

            val = 0
            if phno < len(optrigs):
                phtrigs = optrigs[phno]
                repeated = hasreps(phtrigs)
                if repeated:
                    err(f"Trigger '{repeated}' occurs more than once for opcode '{opc}' in phase {str(phno)}")

                for trig in phtrigs:
                    if trig not in trval:
                        err("Undeclared trigger '" + trig + "' for op-code '" + opc + "'")
                    val |= trval[trig]

            if phno == len(optrigs) - 1:  # last phase for op
                val |= trval['CUT']  # tell sequencer to cut the sequence

            if val > 0:
                content[phno].append(val)
            else:
                content[phno].append(fill_value)

    bitspp = log2(len(rules))
    reqlength = 2 ** bitspp
    aligned = [part + (reqlength - len(part)) * [0] for part in content]
    mmap = reduce(lambda x, y: x + y, aligned, [])

    body = synth(
        opcodes=opcodes,
        triggers=triggers,
        seqwidth=seqwidth,
        phases=phases,
        rom_content=mmap
    )

    with open(fname + '.circ', 'w') as outfile:
        outfile.write(preamble + '\n'.join(body) + epilog)

    if args.gen_image:

        print_colored("Generated ROM image: " + fname + ".img", Fore.BLUE)

        with open(fname + '.img', 'w') as outfile:
            outfile.write('v2.0 raw\n')

            for byte in mmap:
                outfile.write(format(byte, "2x").replace(' ', '0') + '\n')

    print_colored("Success!", Fore.GREEN)


if __name__ == "__main__":
    main()
