from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from _typeshed import SupportsRead


def read(f: SupportsRead[bytes], length: int) -> tuple[int, bytes]:
    try:
        b = f.read(length)
    except EOFError:
        return (0, b"")

    return len(b), b


# WIP
