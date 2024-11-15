import xml.etree.ElementTree as ET

import json


def write_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    # return list(root.iter())

    persons = []
    """[
    dict((attr.tag, attr.text) for attr in person)
    for person in persons
]"""
    for person in root:
        data = {child.tag: child.text for child in person}
        persons.append(data)

    return persons


xml_data = read_xml('PersonData.xml')
print(xml_data)

write_json(xml_data, 'data.json')
