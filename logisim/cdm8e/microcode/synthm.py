__author__ = 'comqas'

########################### command line args
import argparse
from functools import reduce




############################################


def log2(k):
    res = 0
    x = 1  # x=2**res, invariant
    while x < k:
        res += 1
        x = x * 2
    # x>=k, res>=log(k)
    return res


def synt(opcodes=[], seqwidth=3, phases=2, triggers=[], ROM=[0], xwest = 110, ywest = 90, inhibit=False):
    content = ROM
    body = []

    def tunnel(name, x, y, facing='east', width=1):
        return \
            """<comp lib="0" loc="(%d,%d)" name="Tunnel">
          <a name="label" val="%s"/>
          <a name="facing" val="%s"/>
          <a name="labelfont" val="SansSerif plain 9"/>
          <a name="width" val="%d"/>

    </comp>""" % (x, y, name, facing, width)

    def splitter(x, y, mult, facing='east', appearance="center"):
        return \
            """<comp lib="0" loc="(%d,%d)" name="Splitter">
          <a name="fanout" val="%d"/>
          <a name="incoming" val="%d"/>
          <a name="facing" val="%s"/>
          <a name="appear" val="%s"/>
    </comp>""" % (x, y, mult, mult, facing, appearance)

    def encoder(x, y, width):
        return \
            """<comp lib="2" loc="(%d,%d)" name="Priority Encoder">
          <a name="disabled" val="0"/>
          <a name="select" val="%d"/>
    </comp>""" % (x, y, width)

    def ground(x, y):
        return \
            """<comp lib="0" loc="(%d,%d)" name="Ground">
          <a name="facing" val="west"/>
    </comp>""" % (x, y)

    def ROM(x, y, a, d, cont):
        return (
                       """<comp lib="4" loc="(%d,%d)" name="ROM">
          <a name="addrWidth" val="%d"/>
          <a name="dataWidth" val="%d"/>
        <a name="contents">addr/data: %d %d
    """ + ' '.join([format(w, "2x") for w in cont]) + """
    </a>
        </comp>
    """) % (x, y, a, d, a, d)

    def wire(x0, y0, x1, y1):
        return '<wire from="(%d,%d)" to="(%d,%d)"/>' % (x0, y0, x1, y1)


    Ninp = len(opcodes)

    phasebits = log2(phases)

    if phasebits > seqwidth:
        raise ValueError(
            "Can't accommodate " + str(phases) + " execute phases using " + str(seqwidth) + "-bit sequencer")

    bitwidth = log2(Ninp)
    Nhalf = 2 ** (bitwidth - 1)
    Nfull = 2 * Nhalf

    xenc = xwest + Nfull * 5 + 50  # east edge
    yenc = ywest + Nfull * 10 - 20  # centre

    body.append(encoder(xenc, yenc, log2(Ninp)))
    for k in range(Ninp):
        body.append(tunnel(opcodes[k], xwest, ywest + 20 * k))  # input tunnels

    einp0x = xenc - 40
    einp0y = yenc - 10 * (Nhalf - 1)

    for j in range(Nhalf):
        body.append(wire(xwest, ywest + 20 * j, einp0x - (j + 1) * 10, ywest + 20 * j))
        body.append(wire(einp0x - (j + 1) * 10, ywest + 20 * j, einp0x - (j + 1) * 10, einp0y + 10 * j))
        body.append(wire(einp0x - (j + 1) * 10, einp0y + 10 * j, einp0x, einp0y + 10 * j))

    for j in range(Nhalf, Ninp):
        body.append(wire(xwest, ywest + 20 * j, einp0x - (Nfull - j) * 10, ywest + 20 * j))
        body.append(wire(einp0x - (Nfull - j) * 10, ywest + 20 * j, einp0x - (Nfull - j) * 10, einp0y + 10 * j))
        body.append(wire(einp0x - (Nfull - j) * 10, einp0y + 10 * j, einp0x, einp0y + 10 * j))

    if Ninp != Nfull:
        for j in range(Ninp, Nfull):
            body.append(ground(einp0x, einp0y + 10 * j))

    # attach inhibitor (to support Fetch cycle)
    if inhibit:
        body.append(wire(einp0x + 20, einp0y + 10 * Nfull, einp0x + 20, einp0y + 10 * Nfull + 20))
        body.append(tunnel('NonFetch', einp0x + 20, einp0y + 10 * Nfull + 20, facing='north', width=1))

    enc2split = 50  # x-distance between encoder output and splitter

    # route east to splitter
    body.append(wire(xenc, yenc, xenc + enc2split, yenc))
    # split encoder output
    body.append(splitter(xenc + enc2split, yenc, bitwidth, appearance='right'))

    # place phase signal splitter underneath
    seqsplity = yenc + bitwidth * 10 + seqwidth * 10 + 10
    # split sequencer's phase signal
    body.append(splitter(xenc + enc2split, seqsplity, seqwidth, appearance="left"))
    # attach sequencer's tunnel
    body.append(wire(xenc + enc2split, seqsplity, xenc + enc2split, seqsplity + 20))
    body.append(tunnel('phase', xenc + enc2split, seqsplity + 20, facing='north', width=seqwidth))

    # attach receiving splitter (combiner for ROM's A-input)
    body.append(splitter(xenc + enc2split + 40, yenc, bitwidth + phasebits, facing='west', appearance='left'))

    # encoder's "select" output y-coord:
    eoutSy = yenc + 10
    # route encoder's "select" east
    body.append(wire(xenc, eoutSy, xenc + 20, eoutSy))
    # drop south
    body.append(wire(xenc + 20, eoutSy, xenc + 20, eoutSy + 150))

    ROMx = xenc + 260
    # route east
    body.append(wire(xenc + 20, eoutSy + 150, ROMx - 90, eoutSy + 150))
    # route north
    body.append(wire(ROMx - 90, eoutSy + 150, ROMx - 90, eoutSy + 30))
    # connected to sel

    # place ROM
    triglen = len(triggers)
    body.append(ROM(ROMx, yenc, bitwidth + phasebits, triglen, content))
    # connect address line
    body.append(wire(xenc + enc2split + 40, yenc, ROMx - 140, yenc))
    # connect data line
    body.append(wire(ROMx, yenc, ROMx + 10, yenc))
    outsplity = yenc
    body.append(wire(ROMx + 10, yenc, ROMx + 20, yenc))
    outsplitx = ROMx + 20
    # place splitter


    pin0x = outsplitx + 20
    pin0y = outsplity + 10
    pinfy = outsplity + 10 * triglen

    tun0x = pin0x + 10 * triglen
    tun0y = pinfy - 20 * (triglen - 1)

    if tun0y < ywest:
        diff = ywest - tun0y
        pin0y += diff
        tun0y += diff
        body.append(wire(outsplitx, outsplity, outsplitx, outsplity+diff))
        outsplity += diff

    body.append(splitter(outsplitx, outsplity, triglen, appearance='right'))


    for k in range(triglen):
        body.append(tunnel(triggers[k], tun0x, tun0y + 20 * k, facing='west'))  # output tunnels
        body.append(wire(pin0x, pin0y + 10 * k, pin0x + 10 * (k + 1), pin0y + 10 * k))
        body.append(wire(pin0x + 10 * (k + 1), pin0y + 10 * k, pin0x + 10 * (k + 1), tun0y + 20 * k))
        body.append(wire(pin0x + 10 * (k + 1), tun0y + 20 * k, tun0x, tun0y + 20 * k))

    return body, tun0x


def parse(spec):
    rules = []
    first = True
    veryfirst = True
    lnum = 0

    def err(msg):
        print("Error on line %d:" % lnum, msg)
        quit(-1)

    cont = False
    for raw_line in spec.split('\n'):
        lnum += 1
        hashpos = raw_line.find('#')
        if hashpos >= 0:
            raw_line = raw_line[:hashpos]
        raw_line = raw_line.strip()
        if not raw_line: continue
        if cont:
            line += raw_line
        else:
            line = raw_line

        cont = (raw_line[-1] == ',')
        if cont: continue

        line = ''.join(line.split())
        colpos = line.find(':')
        if first:
            if colpos < 0: err("No ':'")
            if veryfirst:
                veryfirst = False
                if line[:colpos]: err("First line defines sequencer width and # of phases, no op-code allowed")
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
            if not opcode: err("Op-code missing")
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
        if colpos >= 0: err("semicolon on previous line requires new phase here; opcode given instead")

        if line[-1] == ';':
            line = line[:-1]
        else:
            first = True
        trigs.append(line.split(','))
        if first:
            rules.append((opcode, trigs))
    return rules, seqwidth, phases, triggers


preamble = \
    """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project source="2.7.1" version="1.0">
This file is intended to be loaded by Logisim (http://www.cburch.com/logisim/).
<lib desc="#Wiring" name="0">
    <tool name="Splitter">
      <a name="facing" val="north"/>
      <a name="fanout" val="1"/>
      <a name="incoming" val="4"/>
      <a name="appear" val="center"/>
      <a name="bit0" val="none"/>
      <a name="bit1" val="none"/>
      <a name="bit2" val="0"/>
      <a name="bit3" val="none"/>
    </tool>
    <tool name="Pin">
      <a name="facing" val="west"/>
      <a name="tristate" val="false"/>
      <a name="label" val="bus 0"/>
    </tool>
    <tool name="Probe">
      <a name="facing" val="south"/>
      <a name="radix" val="16"/>
    </tool>
    <tool name="Tunnel">
      <a name="width" val="8"/>
      <a name="label" val="vec-adr"/>
      <a name="labelfont" val="SansSerif plain 9"/>
    </tool>
    <tool name="Pull Resistor">
      <a name="facing" val="north"/>
    </tool>
    <tool name="Constant">
      <a name="width" val="8"/>
      <a name="value" val="0x80"/>
    </tool>
  </lib>
  <lib desc="#Gates" name="1"/>
  <lib desc="#Plexers" name="2"/>
  <lib desc="#Arithmetic" name="3"/>
  <lib desc="#Memory" name="4">
    <tool name="ROM">
      <a name="contents">addr/data: 8 8
0
</a>
    </tool>
  </lib>
  <lib desc="#I/O" name="5"/>
  <lib desc="#Base" name="6">
    <tool name="Text Tool">
      <a name="text" val=""/>
      <a name="font" val="SansSerif plain 12"/>
      <a name="halign" val="center"/>
      <a name="valign" val="base"/>
    </tool>
  </lib>
  <main name="main"/>
  <options>
    <a name="gateUndefined" val="ignore"/>
    <a name="simlimit" val="1000"/>
    <a name="simrand" val="0"/>
  </options>
  <mappings>
    <tool lib="6" map="Button2" name="Menu Tool"/>
    <tool lib="6" map="Ctrl Button1" name="Menu Tool"/>
    <tool lib="6" map="Button3" name="Menu Tool"/>
  </mappings>
  <toolbar>
    <tool lib="6" name="Poke Tool"/>
    <tool lib="6" name="Edit Tool"/>
    <tool lib="6" name="Text Tool">
      <a name="text" val=""/>
      <a name="font" val="SansSerif plain 12"/>
      <a name="halign" val="center"/>
      <a name="valign" val="base"/>
    </tool>
    <sep/>
    <tool lib="0" name="Pin">
      <a name="tristate" val="false"/>
    </tool>
    <tool lib="0" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="labelloc" val="east"/>
    </tool>
    <tool lib="1" name="NOT Gate"/>
    <tool lib="1" name="AND Gate"/>
    <tool lib="1" name="OR Gate"/>
  </toolbar>
  <circuit name="main">
"""

epilog = \
    """  </circuit>
</project>
"""



def hasreps(x):
    if not x: return ""
    if x[0] not in x[1:]:
        return hasreps(x[1:])
    else:
        return x[0]


def err(msg):
    print(msg)
    quit(-1)





def generate_scheme(data: str, x = 110, y = 90):
    rules, seqwidth, phases, triggers = parse(data)

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

    print("*** SECONDARY DECODER SYNTH ***")

    print("\tSequencer width: ", seqwidth)
    print("\tMaximum phases per instruction: ", phases)
    print("\tTrigger list:")
    print('\t' + (', '.join(["%s(0x%X)" % (tr, trval[tr]) for tr in triggers])))
    print("Processing action lists")

    opc_bits = log2(len(opcodes))

    content = [[] for _ in range(phases)]  # can't use phases*[[]], idiotic Python will create refs to same obj.

    for rule in rules:
        opc, optrigs = rule
        if len(optrigs) > phases:
            err(str(len(optrigs)) + " phases specified for opcode '" + opc + "', greater than maximum declared")
        for phno in range(phases):
            # if args.debug and phno == 0: print('\t' + opc + ':' + '; '.join([', '.join(p) for p in optrigs]))
            val = 0
            if phno < len(optrigs):
                phtrigs = optrigs[phno]
                repeated = hasreps(phtrigs)
                if repeated: err(
                    "Trigger '" + repeated + "' occurs more than once for opcode '" + opc + "' in phase " + str(phno))
                for trig in phtrigs:
                    if trig not in trval:
                        err("Undeclared trigger '" + trig + "' for op-code '" + opc + "'")
                    val += trval[trig]
            if phno == len(optrigs) - 1:  # last phase for op
                val += trval['CUT']  # tell sequencer to cut the sequence
            content[phno].append(val)

    bitspp = log2(len(rules))
    reqlength = 2 ** bitspp
    aligned = [part + (reqlength - len(part)) * [0] for part in content]
    mmap = reduce(lambda x, y: x + y, aligned, [])

    body, next_x = synt(
        opcodes=opcodes,
        triggers=triggers,
        seqwidth=seqwidth,
        phases=phases,
        ROM=mmap,
        xwest=x,
        ywest=y
    )

    return preamble + '\n'.join(body) + epilog, next_x

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Secondary Decoder Synthesis Utility')
    parser.add_argument('-d', dest='debug', action='store_true', default=False,
                        help="provide verbose output for debuggig")
    parser.add_argument('defs', type=str, help="secondary decoder definition file")
    args = parser.parse_args()

    fname = args.defs
    if fname.endswith('.def'): fname = fname[:-4]

    with open(fname + '.def') as fd:
        body, _ = generate_scheme(fd.read())

    with open(fname + '.circ', 'w') as outfile:
        outfile.write(body)
