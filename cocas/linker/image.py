from pathlib import Path
from typing import Union


def write_image(filename: Union[Path, str], arr: bytearray):
    """
    Write the contents or array into file in logisim-compatible format

    :param filename: path to output file
    :param arr: bytearray to be written
    """
    with open(filename, mode='w') as f:
        f.write("v2.0 raw\n")
        zeroes = 0
        for i, byte in enumerate(arr):
            if byte == 0:
                zeroes += 1
            else:
                if zeroes != 0:
                    if zeroes > 4:
                        f.write(f'{zeroes}*00\n')
                        f.write(f'# {i:#2x}\n')
                    else:
                        for _ in range(zeroes):
                            f.write('00\n')
                    zeroes = 0
                f.write(f'{byte:02x}\n')
