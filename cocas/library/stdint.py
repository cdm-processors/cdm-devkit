__all__ = ("sized", "validate")

import dataclasses
import functools
from collections.abc import Mapping
from typing import TypedDict, TypeGuard, TypeVar, cast

DataclassT = TypeVar("DataclassT")


class StdintMetadata(TypedDict):
    range: range


def is_stdint_metadata(m: object) -> TypeGuard[StdintMetadata]:
    if not isinstance(m, Mapping):
        return False

    r = m.get("range")  # pyright: ignore[reportUnknownMemberType]
    return r is not None and isinstance(r, range)


def sized(n: int, unsigned: bool = True) -> StdintMetadata:
    """Set a bit size constraint for an `int` field.

    Remember to use a `stdint.validate` on your dataclass!
    """
    if n <= 0:
        message = f"bit size of int cannot be less than 1, while {n} was provided"
        raise ValueError(message)

    if unsigned:
        return StdintMetadata(range=range(0, 1 << n))

    if n == 1:
        message = "1-bit signed int does not have any meaning"
        raise ValueError(message)

    bound = 1 << (n - 1)
    return StdintMetadata(range=range(-bound, bound))


def validate(cls: type[DataclassT]) -> type[DataclassT]:
    """Modify the provided `dataclasses.dataclass` to validate marked `int` fields."""

    if not dataclasses.is_dataclass(cls):
        message = f"provided class should be a dataclass, while {cls} is not"
        raise TypeError(message)

    collected: dict[str, StdintMetadata] = {}
    for field in dataclasses.fields(cls):
        if is_stdint_metadata(field.metadata):
            collected[field.name] = field.metadata

    if not collected:
        return cls

    init = cls.__init__
    @functools.wraps(init)
    def init_with_validate(
        self, *args, **kwargs,  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    ) -> None:
        init(self, *args, **kwargs)  # pyright: ignore[reportUnknownArgumentType]

        for name, metadata in collected.items():
            value = cast(int, getattr(self, name))  # pyright: ignore[reportUnknownArgumentType]
            if value not in metadata["range"]:
                message = f"field {name} should be in {metadata['range']}, while {value} is not"
                raise ValueError(message)

    cls.__init__ = init_with_validate
    return cls
