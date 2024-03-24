from cocodump.base_types import DecodedSection
from cocodump.targets.cdm16.asm import InstructionGroup, inst_decoders
from cocodump.targets.cdm16.ivt import InterruptVector, ivt_descriptions

from cocodump.targets.cdm16.decoder import decode as cdm16_decode


def append_new_instructions():
    inst_decoders[InstructionGroup.ONE_OP].mnemonics[14] = "ldssp"
    inst_decoders[InstructionGroup.ONE_OP].mnemonics[15] = "stssp"

    inst_decoders[InstructionGroup.TWO_OP].mnemonics[2] = "swpw"
    inst_decoders[InstructionGroup.TWO_OP].mnemonics[3] = "swpb"


def append_new_vectors():
    ivt_descriptions.append(
        InterruptVector(0x14, "_privilege_violation", "Privilege violation")
    )


def decode(image: bytearray, has_ivt: bool = False) -> DecodedSection:

    append_new_instructions()
    append_new_vectors()

    return cdm16_decode(image, has_ivt)
