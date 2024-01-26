from dataclasses import dataclass
from typing import Any, Callable, Type

from cocas.error import CdmException, CdmExceptionTag, CdmTempException
from cocas.object_module import CodeLocation, ObjectSectionRecord
from cocas.targets import CodeSegmentsInterface, TargetInstructionsInterface

from .ast_nodes import (
    AbsoluteSectionNode,
    BreakStatementNode,
    ConditionalStatementNode,
    ContinueStatementNode,
    InstructionNode,
    LabelDeclarationNode,
    LocatableNode,
    RelocatableSectionNode,
    SectionNode,
    UntilLoopNode,
    WhileLoopNode,
)


@dataclass
class CodeBlock:
    def __init__(self, address: int, lines: list,
                 target_instructions: Type[TargetInstructionsInterface],
                 code_segments: Type[CodeSegmentsInterface]):
        self.target_instructions = target_instructions
        self.code_segments = code_segments
        self.address = address
        self.size: int = 0
        self.loop_stack: list = []
        self.segments: list[code_segments.CodeSegment] = []
        self.labels: dict[str, int] = dict()
        self.ents: set[str] = set()
        self.exts: set[str] = set()
        self.code_locations: dict[int, CodeLocation] = dict()
        temp_storage = dict()  # variable to save information for future lines
        self.assemble_lines(lines, temp_storage)
        try:
            # check that everything was ok with this block
            target_instructions.finish(temp_storage)
        except CdmTempException as e:
            # if it isn't ok, must be at least one line
            raise CdmException(CdmExceptionTag.ASM, lines[-1].location.file, lines[-1].location.line, e.message)

    def append_label(self, label_name):
        self.labels[label_name] = self.address + self.size

    def append_branch_instruction(self, location, mnemonic, label_name, inverse=False):
        self.code_locations[self.size] = location
        br = self.target_instructions.make_branch_instruction(location, mnemonic, label_name, inverse)
        self.segments += br
        self.size += sum(map(lambda x: x.size, br))

    def assemble_lines(self, lines: list, temp_storage):
        ast_node_handlers: dict[Type, Callable[[Any, Any], None]] = {
            LabelDeclarationNode: self.assemble_label_declaration,
            InstructionNode: self.assemble_instruction,
            ConditionalStatementNode: self.assemble_conditional_statement,
            WhileLoopNode: self.assemble_while_loop,
            UntilLoopNode: self.assemble_until_loop,
            BreakStatementNode: self.assemble_break_statement,
            ContinueStatementNode: self.assemble_continue_statement,
        }
        for line in lines:
            if isinstance(line, LocatableNode):
                self.code_locations[self.size] = line.location
            ast_node_handlers[type(line)](line, temp_storage)

    def assemble_label_declaration(self, line: LabelDeclarationNode, __):
        label_name = line.label.name
        if (label_name in self.labels or
                label_name in self.ents or
                label_name in self.exts):
            raise Exception(f'Duplicate label "{label_name}" declaration')

        if line.external:
            self.exts.add(label_name)
        else:
            self.append_label(label_name)
            if line.entry:
                self.ents.add(label_name)

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
            raise Exception('"break" not allowed outside of a loop')
        _, finally_label = self.loop_stack[-1]
        self.append_branch_instruction(line.location, 'anything', finally_label)

    def assemble_continue_statement(self, line: ContinueStatementNode, _):
        if len(self.loop_stack) == 0:
            raise Exception('"continue" not allowed outside of a loop')
        cond_label, _ = self.loop_stack[-1]
        self.append_branch_instruction(line.location, 'anything', cond_label)


@dataclass
class Section(CodeBlock):
    def __init__(self, sn: SectionNode,
                 target_instructions: Type[TargetInstructionsInterface],
                 code_segments: Type[CodeSegmentsInterface]):
        if isinstance(sn, AbsoluteSectionNode):
            self.name = '$abs'
            address = sn.address
        elif isinstance(sn, RelocatableSectionNode):
            self.name = sn.name
            address = 0
        else:
            raise Exception('Section is neither Absolute nor Relative, can it happen? It was elif instead of else here')
        super().__init__(address, sn.lines, target_instructions, code_segments)

    def to_object_section_record(self, labels: dict[str, int], templates: dict[str, dict[str, int]]):
        entries = dict(p for p in self.labels.items() if p[0] in self.ents)
        out = ObjectSectionRecord(self.name, self.address, bytearray(), entries, [], self.code_locations)
        for seg in self.segments:
            seg.fill(out, self, labels, templates)
        return out
