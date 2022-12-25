from cocas.ast_nodes import RelocatableExpressionNode
from cocas.default_code_segments import CodeSegmentsInterface
from cocas.location import CodeLocation
from dataclasses import dataclass, field
from cocas.code_block import Section


class CodeSegments(CodeSegmentsInterface):
    @dataclass
    class CodeSegment(CodeSegmentsInterface.CodeSegment):
        pass

    @dataclass
    class RelocatableExpressionSegment(CodeSegment):
        expr: RelocatableExpressionNode

    @dataclass
    class VaryingLengthSegment(CodeSegment):
        is_expanded: bool = field(init=False, default=False)
        expanded_size: int = field(init=False)

    @dataclass
    class BytesSegment(CodeSegment):
        data: bytearray

        def __init__(self, data: bytearray):
            self.data = data
            self.size = len(data)

    @dataclass
    class ShortExpressionSegment(RelocatableExpressionSegment):
        size = 1

    @dataclass
    class ConstExpressionSegment(RelocatableExpressionSegment):
        positive: bool = False
        size = 1

    @dataclass
    class LongExpressionSegment(RelocatableExpressionSegment):
        size = 2

    @dataclass
    class OffsetExpressionSegment(RelocatableExpressionSegment):
        size = 1

    @dataclass
    class BranchInstruction(VaryingLengthSegment):
        branch_mnemonic: str
        expr: RelocatableExpressionNode
        size = 2
        base_size = 2
        expanded_size = 5
