from pathlib import Path


def read_img(file: Path) -> bytearray:
    lines = file.read_text().split('\n')[1:]

    image: bytearray = bytearray()

    for line in lines:

        if line.startswith('#') or len(line) == 0:
            pass
        elif '*' in line:
            (amount, byte) = line.split('*')
            amount = int(amount)
            byte = int(byte, 16)

            for _ in range(amount):
                image.append(byte)
        else:
            image.append(int(line, 16))

    return image
