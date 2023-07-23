from collections.abc import Iterator


def get_label_generator(prefix: str) -> Iterator[str]:
    label_counter = 0

    while True:
        yield f"{prefix}{label_counter}"
        label_counter += 1


_label_generator = get_label_generator("L")


def get_label() -> str:
    return next(_label_generator)
