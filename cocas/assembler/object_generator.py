import itertools
from dataclasses import dataclass
from typing import Any, Union

from cocas.object_module import CodeLocation, ObjectModule, Linkage, concat_rsects

from .ast_nodes import (
    InstructionNode,
    LabelDeclarationNode,
    LabelNode,
    Node,
    ProgramNode,
    RelocatableExpressionNode,
    TemplateFieldNode,
    TemplateSectionNode,
)
from .code_block import Section
from .exceptions import AssemblerException, AssemblerExceptionTag
from .targets import IVaryingLengthSegment, TargetInstructions


@dataclass
class Template:
    def __init__(self, sn: TemplateSectionNode, target_instructions: TargetInstructions):
        self.name: str = sn.name
        self.labels: dict[str, int] = dict()

        size = 0
        temp_storage = dict()
        for line in sn.lines:
            if isinstance(line, LabelDeclarationNode):
                label_name = line.label.name
                if label_name in self.labels:
                    raise AssemblerException(AssemblerExceptionTag.TPLATE, line.location.file, line.location.line,
                                             f'Duplicate label "{label_name}" declaration')
                if line.external:
                    raise AssemblerException(AssemblerExceptionTag.TPLATE, line.location.file, line.location.line,
                                             'External labels not allowed in templates')
                elif line.linkage:
                    raise AssemblerException(AssemblerExceptionTag.TPLATE, line.location.file, line.location.line,
                                             'Ents not allowed in templates')
                else:
                    self.labels[label_name] = size

            elif isinstance(line, InstructionNode):
                if line.mnemonic not in target_instructions.assembly_directives():
                    raise AssemblerException(AssemblerExceptionTag.TPLATE, line.location.file, line.location.line,
                                             'Only these directives allowed in templates: ' +
                                             ', '.join(target_instructions.assembly_directives()))
                for seg in target_instructions.assemble_instruction(line, temp_storage):
                    size += seg.size

        self.labels['_'] = size


def gather_local_labels(sects: list[Section]):
    local_labels = dict()
    for sect in sects:
        local_labels.update({p for p in sect.labels.items() if not p[0].startswith('$')})
    return local_labels


@dataclass
class VaryingLengthEntry:
    seg: IVaryingLengthSegment
    sect: Section
    pos: int
    location: CodeLocation


def update_varying_length(sections: list[Section], known_labels: dict[str, int],
                          template_fields: dict[str, dict[str, int]]):
    labels = gather_local_labels(sections)
    labels.update(known_labels)
    var_len_entries: list[VaryingLengthEntry] = []
    for sect in sections:
        pos = sect.address
        for seg in sect.segments:
            if isinstance(seg, IVaryingLengthSegment):
                a = VaryingLengthEntry(seg, sect, pos, seg.location)
                var_len_entries.append(a)
            pos += seg.size

    changed = True
    while changed:
        changed = False
        for vl in var_len_entries:
            shift = vl.seg.update_varying_length(vl.pos, vl.sect, labels, template_fields)
            if shift:
                for other_vl in var_len_entries:
                    if other_vl.sect is vl.sect and other_vl.pos > vl.pos:
                        other_vl.pos += shift
                changed = True


def label_or_template(label: Union[LabelNode, Any], template_fields: dict[str, dict[str, int]]) -> Node:
    if not isinstance(label, LabelNode):
        return label
    split = label.name.split('.')
    if len(split) > 1 and split[0] in template_fields:
        return TemplateFieldNode(split[0], '.'.join(split[1:]))
    return label


def generate_object_module(pn: ProgramNode, target_instructions: TargetInstructions) -> ObjectModule:
    templates = [Template(t, target_instructions) for t in pn.template_sections]
    template_fields = dict([(t.name, t.labels) for t in templates])
    undefined_file_locals: dict[str, CodeLocation] = dict()

    # LabelDeclarationNode
    # InstructionNode
    # ConditionalStatementNode
    # WhileLoopNode
    # UntilLoopNode
    # BreakStatementNode
    # ContinueStatementNode
    for i in pn.absolute_sections + pn.relocatable_sections:
        for line in i.lines:
            if isinstance(line, LabelDeclarationNode):
                if '.' in line.label.name:
                    prefix = line.label.name.split('.')[0]
                    if prefix in template_fields:
                        raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                                 f"Label {line.label.name} conflicts with template {prefix}")
                if line.external and line.linkage == Linkage.FILE_LOCAL:
                    undefined_file_locals[line.label.name] = line.location
            elif isinstance(line, InstructionNode):
                for arg in line.arguments:
                    if isinstance(arg, RelocatableExpressionNode):
                        arg.add_terms = list(
                            map(lambda x: label_or_template(x, template_fields), arg.add_terms))

    asects = sorted((Section(asect, target_instructions) for asect in pn.absolute_sections), key=lambda s: s.address)
    rsects = [Section(rsect, target_instructions) for rsect in pn.relocatable_sections]

    shared_externals = dict(map(lambda x: (x.label.name, x.linkage), pn.shared_externals))
    for i in itertools.chain(asects, rsects):
        i.exts |= shared_externals
    undefined_file_locals |= { 
        decl.label.name: decl.location 
        for decl in pn.shared_externals 
        if decl.linkage == Linkage.FILE_LOCAL
    }

    for _ in pn.top_instructions:
        pass  # do something

    update_varying_length(asects, {}, template_fields)
    all_labels = gather_local_labels(asects)
    for rsect in rsects:
        update_varying_length([rsect], all_labels, template_fields)

    asect_records = [asect.to_object_section_record(all_labels, template_fields) for asect in asects]
    rsect_records = concat_rsects(map(lambda x: x.to_object_section_record(all_labels, template_fields), rsects))
 
    for section in itertools.chain(asect_records, rsect_records):
        for label in section.entries.keys():
            if label.name in undefined_file_locals:
                undefined_file_locals.pop(label.name)
    
    if undefined_file_locals:
        label, location = next(iter(undefined_file_locals.items()))
        raise AssemblerException(AssemblerExceptionTag.ASM, location.file, location.line,
                                    f'Undefined file-local label: {label}')

    return ObjectModule(asect_records, rsect_records)
