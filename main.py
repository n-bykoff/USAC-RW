from xml_refactor import *
from json_module import *

if __name__ == '__main__':
    template_name = 'testing.xml'

    with open(f'{template_name}', 'r') as f:
        lines = f.readlines()

    params_to_change = {'la': ('text', (12345, 54321, 34567, 33), (22, 28, 22, 28)),
                        'material': (
                            'property', 'name', ('steel123', 'steel123', 'steel123', 'steel123'), (21, 21, 27, 27)),
                        'area': ('property', 'minX', (-120, -100, -120, -300), (35, 38, 35, 38))}

    write_to_json_file(params_to_change, 'params_to_change')

    new_lines = replace_tag_value_from_json(lines, 'params_to_change')
