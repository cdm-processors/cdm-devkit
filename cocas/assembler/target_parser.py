from dataclasses import dataclass

@dataclass
class TargetInfo:
    base: str
    extensions: list[str]

def parse_target(target: str) -> TargetInfo:
    """
    Parse the ``--target`` argument into a :class:`TargetInfo` structure.

    :param target: name of processor, optionally containing concatenated extension letters.
    :return TargetInfo: dataclass containing a base target name and a list of extensions.

    Examples
    --------
    >>> parse_target("cdm-16")
    TargetInfo(base="cdm16", extensions=[])

    >>> parse_target("cdm16em")
    TargetInfo(base="cdm16", extensions=["e", "m"])

    >>> parse_target("8")
    TargetInfo(base="cdm8", extensions=[])

    >>> parse_target("cdm8e")
    TargetInfo(base="cdm8e", extensions=[])
    """
    target = target.replace("-", "").lower()

    if not target.startswith("cdm"):
        target = "cdm" + target

    if target.startswith("cdm16"):
        base = "cdm16"
        suffix = target[len(base):]
    elif target == "cdm8":
        base = "cdm8"
        suffix = ""
    elif target == "cdm8e":
        base = "cdm8e"
        suffix = ""
    else:
        base = target
        suffix = ""

    extensions = list(suffix)
    return TargetInfo(base=base, extensions=extensions)

