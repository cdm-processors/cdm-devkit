from dataclasses import dataclass, field
from typing import Optional

from cocas.object_module import CodeLocation


@dataclass
class Node:
    pass


@dataclass
class RegisterNode(Node):
    number: int


@dataclass
class LabelNode(Node):
    name: str


@dataclass
class LocatableNode(Node):
    def __post_init__(self):
        self.location: CodeLocation = CodeLocation()


@dataclass
class ExportLocationNode(LocatableNode):
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
class InstructionNode(ExportLocationNode):
    mnemonic: str
    arguments: list


@dataclass
class ConditionNode(Node):
    lines: list
    branch_mnemonic: str
    conjunction: Optional[str]
    location: CodeLocation


@dataclass
class ConditionalStatementNode(Node):
    conditions: list[ConditionNode]
    then_lines: list
    else_lines: list
    else_location: Optional[CodeLocation]


@dataclass
class WhileLoopNode(Node):
    condition_lines: list
    branch_mnemonic: str
    lines: list
    while_location: CodeLocation
    stays_location: CodeLocation


@dataclass
class UntilLoopNode(Node):
    lines: list
    branch_mnemonic: str
    until_location: CodeLocation


@dataclass
class BreakStatementNode(ExportLocationNode):
    pass


@dataclass
class ContinueStatementNode(ExportLocationNode):
    pass


@dataclass
class SectionNode(Node):
    lines: list


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
class ProgramNode(Node):
    template_sections: list[TemplateSectionNode]
    relocatable_sections: list[RelocatableSectionNode]
    absolute_sections: list[AbsoluteSectionNode]
    shared_externals: list[LabelNode] = field(default_factory=list)
    top_instructions: list[InstructionNode] = field(default_factory=list)
