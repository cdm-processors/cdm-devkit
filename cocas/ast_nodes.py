from dataclasses import dataclass
from typing import Optional

from cocas.location import CodeLocation


@dataclass
class RegisterNode:
    number: int


@dataclass
class LabelNode:
    name: str


@dataclass
class LocatableNode:
    def __post_init__(self):
        self.location: CodeLocation = CodeLocation()


@dataclass
class TemplateFieldNode(LocatableNode):
    template_name: str
    field_name: str


@dataclass
class RelocatableExpressionNode(LocatableNode):
    byte_specifier: Optional[str]
    add_terms: list
    sub_terms: list
    const_term: int


@dataclass
class LabelDeclarationNode(LocatableNode):
    label: LabelNode
    entry: bool
    external: bool


@dataclass
class InstructionNode(LocatableNode):
    mnemonic: str
    arguments: list


@dataclass
class ConditionNode:
    lines: list
    branch_mnemonic: str
    conjunction: Optional[str]


@dataclass
class ConditionalStatementNode:
    conditions: list
    then_lines: list
    else_lines: list
    cond_location: CodeLocation


@dataclass
class WhileLoopNode:
    condition_lines: list
    branch_mnemonic: str
    lines: list
    mnem_location: CodeLocation


@dataclass
class UntilLoopNode:
    lines: list
    branch_mnemonic: str
    mnem_location: CodeLocation


@dataclass
class BreakStatementNode(LocatableNode):
    pass


@dataclass
class ContinueStatementNode(LocatableNode):
    pass


@dataclass
class SectionNode:
    lines: list
    # location of lines[i] is locations[i]
    locations: list[CodeLocation]

    def __post_init__(self):
        self.line_sources: list[CodeLocation] = []


@dataclass
class AbsoluteSectionNode(SectionNode):
    address: int


@dataclass
class RelocatableSectionNode(SectionNode):
    name: str


@dataclass
class TemplateSectionNode(SectionNode):
    name: str


@dataclass
class ProgramNode:
    template_sections: list[TemplateSectionNode]
    relocatable_sections: list[RelocatableSectionNode]
    absolute_sections: list[AbsoluteSectionNode]
