from util import log2


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


def synth(opcodes, seqwidth, phases, triggers, rom_content, inhibit=False):
    content = rom_content
    body = []

    ywest = 110
    xwest = 90

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
    body.append(splitter(outsplitx, outsplity, triglen, appearance='right'))

    pin0x = outsplitx + 20
    pin0y = outsplity + 10
    pinfy = outsplity + 10 * triglen

    tun0x = pin0x + 10 * triglen
    tun0y = pinfy - 20 * (triglen - 1)

    for k in range(triglen):
        body.append(tunnel(triggers[k], tun0x, tun0y + 20 * k, facing='west'))  # output tunnels
        body.append(wire(pin0x, pin0y + 10 * k, pin0x + 10 * (k + 1), pin0y + 10 * k))
        body.append(wire(pin0x + 10 * (k + 1), pin0y + 10 * k, pin0x + 10 * (k + 1), tun0y + 20 * k))
        body.append(wire(pin0x + 10 * (k + 1), tun0y + 20 * k, tun0x, tun0y + 20 * k))

    return body
