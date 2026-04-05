from dataclasses import dataclass
from typing import Any, Callable, Type

from cocas.object_module import CodeLocation, ObjectSectionRecord, EntryKey, Entry, Linkage

from .ast_nodes import (
    AbsoluteSectionNode,
    BreakStatementNode,
    ConditionalStatementNode,
    ContinueStatementNode,
    ExportLocationNode,
    InstructionNode,
    LabelDeclarationNode,
    Node,
    RelocatableSectionNode,
    SectionNode,
    UntilLoopNode,
    WhileLoopNode,
)
from .exceptions import AssemblerException, AssemblerExceptionTag, CdmTempException
from .targets import ICodeSegment, TargetInstructions


@dataclass
class CodeBlock:
    def __init__(self, address: int, lines: list, target_instructions: TargetInstructions):
        self.target_instructions = target_instructions
        self.address = address
        self.size: int = 0
        self.loop_stack: list = []
        self.segments: list[ICodeSegment] = []
        self.labels: dict[str, int] = dict()
        self.entries: dict[EntryKey, Entry] = dict()
        self.exts: dict[str, Linkage] = dict()
        self.code_locations: dict[int, CodeLocation] = dict()
        temp_storage = dict()  # variable to save information for future lines
        self.assemble_lines(lines, temp_storage)
        try:
            # check that everything was ok with this block
            target_instructions.finish(temp_storage)
        except CdmTempException as e:
            # if it isn't ok, must be at least one line
            raise AssemblerException(AssemblerExceptionTag.ASM, lines[-1].location.file,
                                     lines[-1].location.line, e.message)

    def get_address(self):
        return self.address + self.size

    def append_label(self, label_name: str):
        self.labels[label_name] = self.get_address()

    def append_branch_instruction(self, location, mnemonic, label_name, inverse=False):
        self.code_locations[self.size] = location
        br = self.target_instructions.make_branch_instruction(location, mnemonic, label_name, inverse)
        self.segments += br
        self.size += sum(map(lambda x: x.size, br))

    def assemble_lines(self, lines: list, temp_storage):
        ast_node_handlers: dict[Type[Node], Callable[[Any, Any], None]] = {
            LabelDeclarationNode: self.assemble_label_declaration,
            InstructionNode: self.assemble_instruction,
            ConditionalStatementNode: self.assemble_conditional_statement,
            WhileLoopNode: self.assemble_while_loop,
            UntilLoopNode: self.assemble_until_loop,
            BreakStatementNode: self.assemble_break_statement,
            ContinueStatementNode: self.assemble_continue_statement,
        }
        for line in lines:
            if isinstance(line, ExportLocationNode):
                self.code_locations[self.size] = line.location
            ast_node_handlers[type(line)](line, temp_storage)

    def assemble_label_declaration(self, line: LabelDeclarationNode, __):
        key = EntryKey(line.label.name, line.linkage)
        if line.external:
            self.exts[key.name] = key.linkage
        elif line.linkage == Linkage.WEAK_GLOBAL:
            # We don't know the values of WEAK_GLOBAL labels
            # because these may be overridden at link time.
            # This is why we don't store the address in the
            # known label dictionary and instead add an external declaration.
            self.entries[key] = Entry(self.get_address())
            self.exts[key.name] = Linkage.GLOBAL
        else:
            self.append_label(key.name)
            if line.linkage:
                self.entries[key] = Entry(self.get_address())

    def assemble_instruction(self, line: InstructionNode, temp_storage):
        for seg in self.target_instructions.assemble_instruction(line, temp_storage):
            self.segments.append(seg)
            self.size += seg.size

    def assemble_conditional_statement(self, line: ConditionalStatementNode, temp_storage):
        nonce = self.address + self.size
        or_label = f'${nonce}_or'
        then_label = f'${nonce}_then'
        else_label = f'${nonce}_else'
        finally_label = f'${nonce}_finally'

        next_or = 0
        next_or_label = f'{or_label}{next_or}'
        for cond in line.conditions:
            self.assemble_lines(cond.lines, temp_storage)
            if cond.conjunction is None:
                self.append_branch_instruction(cond.location, cond.branch_mnemonic, else_label, True)
            elif cond.conjunction == 'or':
                self.append_branch_instruction(cond.location, cond.branch_mnemonic, then_label)
                self.append_label(next_or_label)
                next_or += 1
                next_or_label = f'{or_label}{next_or}'
            elif cond.conjunction == 'and':
                self.append_branch_instruction(cond.location, cond.branch_mnemonic, next_or_label, True)

        self.append_label(then_label)
        self.assemble_lines(line.then_lines, temp_storage)

        if len(line.else_lines) > 0:
            self.append_branch_instruction(line.else_location, 'anything', finally_label)
            self.append_label(next_or_label)
            self.append_label(else_label)
            self.assemble_lines(line.else_lines, temp_storage)
            self.append_label(finally_label)
        else:
            self.append_label(next_or_label)
            self.append_label(else_label)

    def assemble_while_loop(self, line: WhileLoopNode, temp_storage):
        nonce = self.address + self.size
        cond_label = f'${nonce}_cond'
        finally_label = f'${nonce}_finally'

        self.loop_stack.append((cond_label, finally_label))
        self.append_label(cond_label)
        self.assemble_lines(line.condition_lines, temp_storage)
        self.append_branch_instruction(line.stays_location, line.branch_mnemonic, finally_label, True)
        self.assemble_lines(line.lines, temp_storage)
        self.append_branch_instruction(line.while_location, 'anything', cond_label)
        self.append_label(finally_label)
        self.loop_stack.pop()

    def assemble_until_loop(self, line: UntilLoopNode, temp_storage):
        nonce = self.address + self.size
        loop_body_label = f'${nonce}_loop_body'
        cond_label = f'${nonce}_cond'
        finally_label = f'${nonce}_finally'
        until_location = line.until_location

        self.loop_stack.append((cond_label, finally_label))
        self.append_label(loop_body_label)
        self.assemble_lines(line.lines, temp_storage)
        self.append_label(cond_label)
        self.append_branch_instruction(until_location, line.branch_mnemonic, loop_body_label, True)
        self.append_label(finally_label)
        self.loop_stack.pop()

    def assemble_break_statement(self, line: BreakStatementNode, _):
        if len(self.loop_stack) == 0:
            raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                     '"break" not allowed outside of a loop')
        _, finally_label = self.loop_stack[-1]
        self.append_branch_instruction(line.location, 'anything', finally_label)

    def assemble_continue_statement(self, line: ContinueStatementNode, _):
        if len(self.loop_stack) == 0:
            raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                     '"continue" not allowed outside of a loop')
        cond_label, _ = self.loop_stack[-1]
        self.append_branch_instruction(line.location, 'anything', cond_label)


@dataclass
class Section(CodeBlock):
    def __init__(self, address: int, lines: list, target_instructions: TargetInstructions):
        super().__init__(address, lines, target_instructions)

    def to_object_section_record(self, labels: dict[str, int], templates: dict[str, dict[str, int]]):
        out = ObjectSectionRecord(self.name, self.address, bytearray(), dict(self.entries), [], self.code_locations)
        for seg in self.segments:
            seg.fill(out, self, labels, templates)
        return out

@dataclass
class AbsoluteSection(Section):
    def __init__(self, sn: SectionNode, target_instructions: TargetInstructions):
        self.name = '$abs'
        super().__init__(sn.address, sn.lines, target_instructions)

@dataclass
class RelocatableSection(Section):
    def __init__(self, name: str, nodes: list[SectionNode], target_instructions: TargetInstructions):
        if not nodes:
            raise ValueError("Node list must not be empty.")
        self.name = name
        super().__init__(0, [line for node in nodes for line in node.lines], target_instructions)
