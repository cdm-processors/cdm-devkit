import string

from colorama.ansi import Fore, Style


def colorize(token: str, color: "Fore | Style") -> str:
    return f"{color}{token}{Style.RESET_ALL}"


SPECIAL_REGISTERS = ["sp", "pc", "fp"]


def colorize_argument(arg: str) -> str:
    if (len(arg) >= 2 and arg.startswith('r') and arg[1].isdigit()) or \
            arg in SPECIAL_REGISTERS:
        return colorize(arg, Style.NORMAL)

    if arg.isdecimal() or (len(arg) > 1 and arg[1:].isdecimal()) or \
            (len(arg) > 2 and arg.startswith("0x") and all(c in string.hexdigits for c in arg[2:])):
        return colorize(arg, Style.NORMAL)

    return colorize(arg, Fore.LIGHTYELLOW_EX)
