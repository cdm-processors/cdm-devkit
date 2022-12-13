from cdm16emu import *

def get_image(file):

    lines = []

    with open(file, 'r') as f:
        lines = f.readlines()

    lines = lines[1:]

    image = []

    for line in lines:
        image.append(int(line, 16))

    return image

"""if __name__ == '__main__':

    mc = []

    image = [ 0x38, 0x07, 0x05, 0x00, 0x38, 0x00, 0x0f, 0x0a, 0x70, 0x66 ]

    with open('cdm16_decoder.img') as f:
        mc = f.readlines()[1:]

    for i, e in enumerate(mc):
        mc[i] = int(e, 16)

    p = Processor(mc)

    m = Memory.from_image(image)
    t = Terminal(0xffff)

    p.attach(m)
    p.attach(t)

    while True:
        p.step()"""

if __name__ == '__main__':

    mc = []

    #image = [ 0x38, 0x07, 0x05, 0x00, 0x38, 0x00, 0x0f, 0x0a, 0x70, 0x66 ]

    #image = [0x08, 0x78, 0xfe, 0xdd]

    image = [ 0x11, 0x20, 0xff, 0xff, 0x08, 0x78, 0xc8, 0x51, 0xfd, 0xdd ]

    with open('cdm16_decoder.img') as f:
        mc = f.readlines()[1:]

    for i, e in enumerate(mc):
        mc[i] = int(e, 16)

    data_bus = Bus("Data Bus")
    address_bus = Bus("Address Bus")

    p = Processor(mc, address_bus, data_bus)

    m = Memory.from_image(address_bus, data_bus, image)

    d = Display(data_bus)

    p.attach(m)
    p.attach(d)

    #p.attach(t)

    while True:
        input()
        p.step()
        print(p)