from collections.abc import Iterable, Mapping, Sequence
from math import ceil, log2
from typing import Self, TypeAlias

from strictyaml import HexInt, Int, MapPattern, Seq, Str, Validator

Integer = Int() | HexInt()
SerializedMemory: TypeAlias = dict[int, int | str | list[int | str]]


class Memory:
    """Implements state-resolving functionality for the memory layout section."""
    _layout: dict[int, int]

    def __init__(self) -> None:
        """Creates an empty layout instance.

        Notice that this method should usually not be used directly. In most cases,
        use ``resolve`` method instead.
        """
        self._layout = {}

    @property
    def layout(self) -> Mapping[int, int]:
        """Get a mapping-shaped memory layout.

        Each key corresponds to the specified memory byte, while each value is
        an ``int`` in range from ``0`` to ``255``.

        Returns:
            A mapping.
        """
        return self._layout

    @staticmethod
    def schema() -> Validator:
        """A ``strictyaml.Validator`` schema for state loading from YAML document.

        Returns:
            The YAML schema for user-defined memory layout.
        """
        return MapPattern(HexInt(), Integer | Str() | Seq(Integer | Str()))

    @staticmethod
    def resolve_integer(val: int, addr: int = 0) -> list[int]:
        """Converts ``val`` int to a list of byte-ranged ints.

        Args:
            val:
                A non-negative int to convert.
            addr:
                An address of int. Can be passed for richer exceptions.

        Returns:
            A list of byte-ranged ints.

        Raises:
            ValueError:
                If ``val`` is negative.
        """
        if val < 0:
            raise ValueError(f"{val = } at {addr:0X} can't be negative")

        byte_length = 2 ** ceil(log2(ceil(val.bit_length() / 8)))
        return list(val.to_bytes(byte_length, "little", signed=False))

    @staticmethod
    def resolve_string(val: str, addr: int = 0) -> list[int]:
        """Converts ``val`` ASCII string to a list of byte-ranged ints.

        Args:
            val:
                An ASCII string to convert.
            addr:
                An address of string. Can be passed for richer exceptions.

        Returns:
            A list of byte-ranged ints.

        Raises:
            ValueError:
                If ``val`` isn't an ASCII string.
        """
        if not val.isascii():
            raise ValueError(f"{val = } at {addr:0X} isn't an ASCII string")

        return [ord(char) for char in val]

    @classmethod
    def resolve_vector(cls, val: Iterable[int | str], addr: int = 0) -> list[int]:
        """Converts ``val`` vector of literals to a list of byte-ranged ints, where
        literal is an int or a string.

        Args:
            val:
                A vector to convert.
            addr:
                An address of string. Can be passed for richer exceptions.

        Returns:
            A list of byte-ranged ints.

        Raises:
            ValueError:
                If resolving of an int or a string failed OR a given vector contains
                a nested vectors OR a given vector contains an unknown literal.
        """
        resolved_vector: list[int] = []
        for literal in val:
            match literal:
                case int():
                    resolved_literal = cls.resolve_integer(literal, addr)
                case str():
                    resolved_literal = cls.resolve_string(literal, addr)
                case list():
                    raise ValueError(f"nested vector at {addr:0X} isn't supported")
                case _:
                    raise ValueError(f"{literal = } at {addr:0X} can't be parsed")

            resolved_vector.extend(resolved_literal)
            addr += len(resolved_literal)

        return resolved_vector

    @staticmethod
    def is_only_bytes(val: Sequence[int]) -> int | None:
        """Checks if all ints in a given list are byte-ranged.

        Args:
            val:
                A list of ints.

        Returns:
            ``None``, if all bytes are byte-ranged, index of invalid int otherwise.
        """
        for idx, byte in enumerate(val):
            if not 0 <= byte <= 255:
                raise idx

        return None

    def unsafe_write(self, addr: int, val: Iterable[int]) -> int:
        """Writes a byte list from a specified address.

        Notice that this method does not check if a given list really contains only
        byte-ranged ints, so you should check this yourself or use a simple ``write``
        method.

        Args:
            addr:
                An address from which bytes will be written.
            val:
                A list of byte-ranged ints.

        Returns:
            An address where the write process can be continued.

        Raises:
            ValueError:
                If there is a memory overlap, that is, if you are trying to write to
                already initialized memory.
        """
        for byte in val:
            if addr in self._layout:
                raise ValueError(f"encountered conflict at {addr:0X}")

            self._layout[addr] = byte
            addr += 1

        return addr

    def write(self, addr: int, val: Sequence[int]) -> int:
        """Checks if ``val`` is a byte-ranged int list and if it is, writes it from a
        specified address.

        Args:
            addr:
                An address from which bytes will be written.
            val:
                A list of byte-ranged ints.

        Returns:
            An address where the write process can be continued.

        Raises:
            ValueError:
                If a some int in a given list isn't byte-ranged, or if there is a
                memory overlap, that is, if you are trying to write to already
                initialized memory.
        """
        if (idx := self.is_only_bytes(val)) is not None:
            raise ValueError(f"byte = {val[idx]}")

        return self.unsafe_write(addr, val)

    @classmethod
    def resolve(cls, raw_layout: SerializedMemory) -> Self:
        """Creates a ``Memory`` instance from user-defined layout.

        Args:
            raw_layout:
                A user-defined layout of memory.

        Returns:
            A ``Memory`` instance.

        Raises:
            ValueError:
                If ``raw_layout`` contains invalid literals or overlapping sections.
        """
        memory = cls()

        for addr, scalar in raw_layout.items():
            match scalar:
                case int():
                    resolved_scalar = cls.resolve_integer(scalar, addr)
                case str():
                    resolved_scalar = cls.resolve_string(scalar, addr)
                case list():
                    resolved_scalar = cls.resolve_vector(scalar, addr)
                case _:
                    raise TypeError(f"encountered unknown {scalar = } at {addr:0X}")

            memory.unsafe_write(addr, resolved_scalar)

        return memory
