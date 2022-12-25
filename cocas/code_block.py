from dataclasses import dataclass

from cocas.ast_nodes import RelocatableExpressionNode, LabelNode, LabelDeclarationNode, InstructionNode, \
    ConditionalStatementNode, WhileLoopNode, UntilLoopNode, SaveRestoreStatementNode, BreakStatementNode, \
    ContinueStatementNode, GotoStatementNode, LocatableNode, RegisterNode, SectionNode, AbsoluteSectionNode, \
    RelocatableSectionNode
# from cocas.code_segments import CodeSegment, BranchInstruction

from cocas import default_instructions, default_code_segments
from cocas.location import CodeLocation


@dataclass
class CodeBlock:
    def __init__(self, address: int, lines: list,
                 target_instructions: default_instructions.TargetInstructionsInterface,
                 code_segments: default_code_segments.CodeSegmentsInterface):
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
        self.assemble_lines(lines)

    def append_label(self, label_name):
        self.labels[label_name] = self.address + self.size

    def append_branch_instruction(self, mnemonic, label_name):
        self.segments.append(
            self.code_segments.BranchInstruction(mnemonic, RelocatableExpressionNode(None, [LabelNode(label_name)], [], 0)))
        self.size += self.code_segments.BranchInstruction.base_size

    def assemble_lines(self, lines: list):
        ast_node_handlers = {
            LabelDeclarationNode: self.assemble_label_declaration,
            InstructionNode: self.assemble_instruction,
            ConditionalStatementNode: self.assemble_conditional_statement,
            WhileLoopNode: self.assemble_while_loop,
            UntilLoopNode: self.assemble_until_loop,
            SaveRestoreStatementNode: self.assemble_save_restore_statement,
            BreakStatementNode: self.assemble_break_statement,
            ContinueStatementNode: self.assemble_continue_statement,
            GotoStatementNode: self.assemble_branch_instructions
        }
        for line in lines:
            if isinstance(line, LocatableNode):
                self.code_locations[self.size] = line.location
            ast_node_handlers[type(line)](line)

    def assemble_label_declaration(self, line: LabelDeclarationNode):
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

    def assemble_instruction(self, line: InstructionNode):
        for seg in self.target_instructions.assemble_instruction(line, self.code_segments):
            self.segments.append(seg)
            self.size += seg.size

    def assemble_conditional_statement(self, line: ConditionalStatementNode):
        nonce = self.address + self.size
        or_label = f'${nonce}_or'
        then_label = f'${nonce}_then'
        else_label = f'${nonce}_else'
        finally_label = f'${nonce}_finally'

        next_or = 0
        for cond in line.conditions:
            self.assemble_lines(cond.lines)
            next_or_label = f'{or_label}{next_or}'
            if cond.conjunction is None:
                self.append_branch_instruction(f'n{cond.branch_mnemonic}', else_label)
            elif cond.conjunction == 'or':
                self.append_branch_instruction(cond.branch_mnemonic, then_label)
                self.append_label(next_or_label)
                next_or += 1
            elif cond.conjunction == 'and':
                self.append_branch_instruction(f'n{cond.branch_mnemonic}', next_or_label)

        self.append_label(then_label)
        self.assemble_lines(line.then_lines)

        if len(line.else_lines) > 0:
            self.append_branch_instruction('anything', finally_label)
            self.append_label(else_label)
            self.assemble_lines(line.else_lines)
            self.append_label(finally_label)
        else:
            self.append_label(else_label)

    def assemble_while_loop(self, line: WhileLoopNode):
        nonce = self.address + self.size
        cond_label = f'${nonce}_cond'
        finally_label = f'${nonce}_finally'

        self.loop_stack.append((cond_label, finally_label))
        self.append_label(cond_label)
        self.assemble_lines(line.condition_lines)
        self.append_branch_instruction(f'n{line.branch_mnemonic}', finally_label)
        self.assemble_lines(line.lines)
        self.append_branch_instruction('anything', cond_label)
        self.append_label(finally_label)
        self.loop_stack.pop()

    def assemble_until_loop(self, line: UntilLoopNode):
        nonce = self.address + self.size
        loop_body_label = f'${nonce}_loop_body'
        cond_label = f'${nonce}_cond'
        finally_label = f'${nonce}_finally'

        self.loop_stack.append((cond_label, finally_label))
        self.append_label(loop_body_label)
        self.assemble_lines(line.lines)
        self.append_label(cond_label)
        self.append_branch_instruction(f'n{line.branch_mnemonic}', loop_body_label)
        self.append_label(finally_label)
        self.loop_stack.pop()

    def assemble_save_restore_statement(self, line: SaveRestoreStatementNode):
        rn = line.saved_register.number
        push = InstructionNode('push', [RegisterNode(rn)])
        pop = InstructionNode('pop', [RegisterNode(rn)])
        self.assemble_instruction(push)
        self.assemble_lines(line.lines)
        self.assemble_instruction(pop)

    def assemble_break_statement(self, _: BreakStatementNode):
        if len(self.loop_stack) == 0:
            raise Exception('"break" not allowed outside of a loop')
        _, finally_label = self.loop_stack[-1]
        self.append_branch_instruction('anything', finally_label)

    def assemble_continue_statement(self, _: ContinueStatementNode):
        if len(self.loop_stack) == 0:
            raise Exception('"continue" not allowed outside of a loop')
        cond_label, _ = self.loop_stack[-1]
        self.append_branch_instruction('anything', cond_label)

    def assemble_branch_instructions(self, line: GotoStatementNode):
        self.segments.append(self.code_segments.BranchInstruction(line.branch_mnemonic, line.expr))
        self.segments[-1].location = line.location
        self.size += self.code_segments.BranchInstruction.base_size


@dataclass
class Section(CodeBlock):
    def __init__(self, sn: SectionNode,
                 target_instructions: default_instructions.TargetInstructionsInterface,
                 code_segments: default_code_segments.CodeSegmentsInterface):
        if isinstance(sn, AbsoluteSectionNode):
            self.name = '$abs'
            address = sn.address
        elif isinstance(sn, RelocatableSectionNode):
            self.name = sn.name
            address = 0
        else:
            raise Exception('Section is neither Absolute nor Relative, can it happen? It was elif instead of else here')
        super().__init__(address, sn.lines, target_instructions, code_segments)
