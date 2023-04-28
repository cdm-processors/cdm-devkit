from colorama import Fore

from .args import args


def parse(spec):
    rules = []
    first = True
    veryfirst = True
    lnum = 0

    def err(msg):
        if args.color:
            print(Fore.RED + "Error on line " + str(lnum) + ": " + msg + Fore.RESET)
        else:
            print("Error on line %d:" % lnum, msg)

        quit(-1)

    cont = False
    for raw_line in spec.split('\n'):
        lnum += 1
        hashpos = raw_line.find('#')
        if hashpos >= 0:
            raw_line = raw_line[:hashpos]
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        if cont:
            line += raw_line
        else:
            line = raw_line

        cont = (raw_line[-1] == ',')
        if cont:
            continue

        line = ''.join(line.split())
        colpos = line.find(':')
        if first:
            if colpos < 0:
                err("No ':'")
            if veryfirst:
                veryfirst = False
                if line[:colpos]:
                    err("First line defines sequencer width and # of phases, no op-code allowed")
                pars = line[colpos + 1:]
                pars = pars.split(',')
                if len(pars) < 2 or not pars[0].isdigit() or not pars[1].isdigit():
                    err("Expected two numbers separated by ',' on first line: <seq.width>,<# of phases>")
                seqwidth = int(pars[0])
                phases = int(pars[1])
                triggers = list(pars[2:])
                if not triggers:
                    err("Expected trigger list to follow seq and phases, found none")
                continue
            first = False
            opcode = line[:colpos]
            if not opcode:
                err("Op-code missing")
            rest = line[colpos + 1:]
            if not rest:
                print("WARNING: No-op specified for ", opcode)
                first = True
                trigs = []
            else:
                if rest[-1] == ';':
                    rest = rest[:-1]
                else:
                    first = True
                trigs = [rest.split(',')]
            if first:
                rules.append((opcode, trigs))
            continue
        if colpos >= 0:
            err("semicolon on previous line requires new phase here; opcode given instead")

        if line[-1] == ';':
            line = line[:-1]
        else:
            first = True
        trigs.append(line.split(','))
        if first:
            rules.append((opcode, trigs))
    return rules, seqwidth, phases, triggers
