from dataclasses import dataclass
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
    byte_specifier: str | None
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
    conjunction: str


@dataclass
class ConditionalStatementNode:
    conditions: list
    then_lines: list
    else_lines: list


@dataclass
class WhileLoopNode:
    condition_lines: list
    branch_mnemonic: str
    lines: list


@dataclass
class UntilLoopNode:
    lines: list
    branch_mnemonic: str


@dataclass
class BreakStatementNode(LocatableNode):
    pass


@dataclass
class ContinueStatementNode(LocatableNode):
    pass


@dataclass
class SaveRestoreStatementNode:
    saved_register: RegisterNode
    lines: list
    restored_register: RegisterNode


@dataclass
class GotoStatementNode(LocatableNode):
    branch_mnemonic: str
    expr: RelocatableExpressionNode


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
