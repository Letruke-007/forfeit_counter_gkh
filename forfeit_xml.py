import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='UTF-8')

tree = ET.parse('files/data.xml', parser)
root = tree.getroot()

new_list = root.findall('PLANT')
#
# for row in new_list:
#     print(row.find('COMMON').text)
#
# print(f'In this file {len(new_list)} plants')

common_list = root.findall('PLANT/COMMON')

for row in common_list:
    print(row.text)

tree.write('files/result.xml', encoding='UTF-8')
