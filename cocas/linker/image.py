from collections.abc import Callable
from pathlib import Path
from typing import Union

WriterFn = Callable[[Path, bytearray], None]


def write_binary_image(filename: Path, arr: bytearray):
    with open(filename, mode='wb') as f:
        f.write(arr)


def write_logisim_image(filename: Path, arr: bytearray):
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


DEFAULT_WRITER = write_binary_image

IMAGE_WRITERS: dict[str, WriterFn] = {
    '.bin': write_binary_image,
    '.img': write_logisim_image,
}


def write_image(filename: Union[Path, str], arr: bytearray):
    """
    Write the contents of array into file in format
    that is derived from extension.
    If extension is unknown then format is defaulted
    to binary.

    :param filename: path to output file
    :param arr: bytearray to be written
    """

    if not isinstance(filename, Path):
        filename = Path(filename)

    writer = IMAGE_WRITERS.get(filename.suffix, DEFAULT_WRITER)

    writer(filename, arr)
