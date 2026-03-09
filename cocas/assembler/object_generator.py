import itertools
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Union

from cocas.object_module import CodeLocation, ObjectModule, Linkage

from .ast_nodes import (
    SectionNode,
    AbsoluteSectionNode,
    RelocatableSectionNode,
    InstructionNode,
    LabelDeclarationNode,
    LabelNode,
    Node,
    ProgramNode,
    RelocatableExpressionNode,
    TemplateFieldNode,
    TemplateSectionNode,
)
from .code_block import AbsoluteSection, RelocatableSection
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
                                             f'Duplicate definition of label "{label_name}" in template')
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


def apply_templates(section_nodes: list[SectionNode], template_fields: dict[str, dict[str,int]]):
    for i in section_nodes:
        for line in i.lines:
            if not isinstance(line, InstructionNode):
                continue
            for arg in line.arguments:
                if not isinstance(arg, RelocatableExpressionNode):
                    continue
                arg.add_terms = list(map(lambda x: label_or_template(x, template_fields), arg.add_terms))


def group_rsects(nodes: list[RelocatableSectionNode]) -> dict[str, list[RelocatableSectionNode]]:
    grouped = defaultdict(list)
    for node in nodes:
        grouped[node.name].append(node)
    return grouped


def validate_labels(section_nodes: list[SectionNode], template_fields: set[str]) :
    section_labels: dict[Union[str, int], dict[str, CodeLocation]] = defaultdict(dict)
    global_labels: dict[str, CodeLocation] = dict()
    file_local_labels: dict[str, CodeLocation] = dict()
    file_local_exts: dict[str, CodeLocation] = dict()

    for i in section_nodes:
        section_key: Union[str, int]
        match i:
            case AbsoluteSectionNode():
                section_key = i.address
            case RelocatableSectionNode():
                section_key = i.name
        for line in i.lines:
            if not isinstance(line, LabelDeclarationNode):
                continue
            if '.' in line.label.name:
                prefix = line.label.name.split('.')[0]
                if prefix in template_fields:
                    raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                             f'Label "{line.label.name}" conflicts with template "{prefix}"')

            if line.label.name in section_labels[section_key]:
                first_line = section_labels[section_key][line.label.name].line
                raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                         (f'Duplicate definition of label "{line.label.name}" in section\n'
                                          f'First definition at line {first_line}'))

            section_labels[section_key][line.label.name] = line.location
            match line.linkage, line.external:
                case Linkage.FILE_LOCAL, True:
                    file_local_exts[line.label.name] = line.location
                case Linkage.GLOBAL, False:
                    if line.label.name in global_labels:
                        first_line = global_labels[line.label.name].line
                        raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                                 (f'Duplicate definition of global label "{line.label.name}" in file\n'
                                                  f'First definition at line {first_line}'))
                    global_labels[line.label.name] = line.location
                case Linkage.FILE_LOCAL, False:
                    if line.label.name in file_local_labels:
                        first_line = file_local_labels[line.label.name].line
                        raise AssemblerException(AssemblerExceptionTag.ASM, line.location.file, line.location.line,
                                                 (f'Duplicate definition of file-local label "{line.label.name}" in file\n'
                                                  f'First definition at line {first_line}'))
                    file_local_labels[line.label.name] = line.location

    for name in set(file_local_exts) - set(file_local_labels):
        location = file_local_exts[name]
        raise AssemblerException(AssemblerExceptionTag.ASM, location.file, location.line,
                                 f'Undefined file-local label "{name}"')

def generate_object_module(pn: ProgramNode, target_instructions: TargetInstructions) -> ObjectModule:
    templates = [Template(t, target_instructions) for t in pn.template_sections]
    template_fields = dict([(t.name, t.labels) for t in templates])
    shared_externals = dict(map(lambda x: (x.label.name, x.linkage), pn.shared_externals))
    section_nodes = pn.absolute_sections + pn.relocatable_sections

    validate_labels(section_nodes, template_fields.keys())
    apply_templates(section_nodes, template_fields)

    asects = [AbsoluteSection(asect, target_instructions) 
              for asect in sorted(pn.absolute_sections, key=lambda s: s.address)]
    rsects = [RelocatableSection(name, nodes, target_instructions) 
              for name, nodes in group_rsects(pn.relocatable_sections).items()]
    for i in itertools.chain(asects, rsects):
        i.exts |= shared_externals

    for _ in pn.top_instructions:
        pass  # do something

    update_varying_length(asects, {}, template_fields)
    all_labels = gather_local_labels(asects)
    for rsect in rsects:
        update_varying_length([rsect], all_labels, template_fields)

    asect_records = [asect.to_object_section_record(all_labels, template_fields) for asect in asects]
    rsect_records = [rsect.to_object_section_record(all_labels, template_fields) for rsect in rsects]

    return ObjectModule(asect_records, rsect_records)
