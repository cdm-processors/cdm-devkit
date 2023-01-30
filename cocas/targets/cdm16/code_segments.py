from dataclasses import dataclass

from cocas.default_code_segments import CodeSegmentsInterface


class CodeSegments(CodeSegmentsInterface):
    @dataclass
    class CodeSegment(CodeSegmentsInterface.CodeSegment):
        pass

    class VaryingLengthSegment(CodeSegment, CodeSegmentsInterface.VaryingLengthSegment):
        pass

    @dataclass
    class BytesSegment(CodeSegment):
        data: bytearray
