from cocas.ast_nodes import RelocatableExpressionNode
from cocas.location import CodeLocation
from dataclasses import dataclass, field


@dataclass
class CodeSegment:
    base_size: int = field(init=False)

    def __post_init__(self):
        # ugly hack to store code location in segments
        # now this whole project is one big and ugly hack
        self.location: CodeLocation = CodeLocation()


@dataclass
class RelocatableExpressionSegment(CodeSegment):
    expr: RelocatableExpressionNode


@dataclass
class VariableLengthSegment(CodeSegment):
    is_expanded: bool = field(init=False, default=False)
    expanded_size: int = field(init=False)


@dataclass
class BytesSegment(CodeSegment):
    data: bytearray

    def __init__(self, data: bytearray):
        self.data = data
        self.base_size = len(data)


@dataclass
class ShortExpressionSegment(RelocatableExpressionSegment):
    base_size = 1


@dataclass
class ConstExpressionSegment(RelocatableExpressionSegment):
    positive: bool = False
    base_size = 1


@dataclass
class LongExpressionSegment(RelocatableExpressionSegment):
    base_size = 2


@dataclass
class OffsetExpressionSegment(RelocatableExpressionSegment):
    base_size = 1


@dataclass
class BranchInstruction(VariableLengthSegment):
    branch_mnemonic: int
    expr: RelocatableExpressionNode
    base_size = 2
    expanded_size = 5
