import xml.etree.ElementTree as ET
from synthm import generate_scheme
import os
import shutil

file_name = 'CdM-8-mark5-full.circ'
circuit_name = 'CdM_8_mark5'
label_text = 'decoder_here'
backup_dir = 'backup'


def_files = ['CdM8-2ph.def', 'CdM8-ext.def']


max_num = 0
for file in os.listdir(backup_dir):
    if file.endswith('.circ'):
        try:
            max_num = max(max_num, int(file.split('.')[0]))
        except ValueError:
            pass

shutil.copyfile(file_name, f'{backup_dir}/{max_num+1}.circ')



tree = ET.parse(file_name)
project = tree.getroot()
circuits = project.findall('circuit')

circuit = list(filter(lambda a: a.attrib['name'] == circuit_name, circuits))[0]


def parse_loc(loc: str)->tuple[int]:
    return tuple(map(int, loc[1:-1].split(',')))

mark_position = None



for component in circuit.findall('comp'):
    for a in component.findall('a'):
        if a.attrib['name'] == 'text' and a.attrib['val'] == label_text:
            mark_position = parse_loc(component.attrib['loc'])


if mark_position is None:
    print("Could not find mark")
    quit(0)

print(mark_position)


def should_remove(loc: str) -> bool:
    loc = parse_loc(loc)
    return loc[0] > mark_position[0] and loc[1] > mark_position[1]


for component in circuit.findall('comp'):
    loc = component.attrib['loc']
    if should_remove(loc):
        circuit.remove(component)

for wire in circuit.findall('wire'):
    loc1 = wire.attrib['from']
    loc2 = wire.attrib['to']
    if should_remove(loc1) and should_remove(loc2):
        circuit.remove(wire)



next_x = mark_position[0]

for i, def_file in enumerate(def_files):
    next_x += 100
    with open(def_file, 'r') as fd:
        def_data = fd.read()
    xml_data, next_x = generate_scheme(def_data, next_x, mark_position[1] + 50)
    gen_project = ET.fromstring(xml_data)
    gen_circuit = gen_project.find('circuit')
    for element in gen_circuit.iter():
        circuit.append(element)




tree.write(file_name)
pass

