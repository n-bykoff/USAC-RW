import pickle

class Tag:

    def __init__(self, name, tabs, *args):
        with open('t&t.pickle', 'rb') as f:
            tags_and_types = pickle.load(f)

        self.name = name
        self.tag_type = tags_and_types[name]
        self.params = args[0]
        self.tabs = tabs


    def create_string(self):
        params = self.params
        name = self.name

        with open('t&p.pickle', 'rb') as f:
            tags_and_params = pickle.load(f)

        if self.tag_type == 'double':
            string = self.tabs * '\t' + f'<{name}'

            params_names = tags_and_params[name]
            if len(params_names) > 0:
                for i in range(len(params_names)):
                    string += f' {params_names[i]}="{params[i]}"'

            string += '>*\n' + self.tabs * '\t' + f'</{name}>#'
            
            # костыль
            if name == 'body':
                string = string.replace('#', '')

        elif self.tag_type == 'inline':
            string = self.tabs * '\t' + f'<{name}'

            params_names = tags_and_params[name]
            for i in range(len(params)):
                string += f' {params_names[i]}="{params[i]}"'

            string += f' />*'

        return string


def make_xml(tags, file_name):
    string = ''

    for tag_name in tags.keys():
        tabs = tags[tag_name][0] - 1
        tag = Tag(tag_name, tabs, tags[tag_name][1])

        if tabs == 0:
            string += tag.create_string()
            string = string.replace('#', '')
            prev_tabs = tabs
        else:
            adding_string = tag.create_string()
            if tabs >= prev_tabs:
                string = string.replace('*', f'\n{adding_string}')
                prev_tabs = tabs
            elif tabs < prev_tabs:
                string = string.replace('*', '')
                string = string.replace('#', f'\n{adding_string}')
                prev_tabs = tabs

    string = string.replace('#', '')
    string = string.replace('*', '')

    with open(f'{file_name}.xml', 'w') as f:
        f.write(string)


if __name__ == '__main__':
    tags = {'task': [1, [150, 1]], 
    'system': [2, []], 
    'meshMovement': [3, ['none']], 'timeStep': [3, [1.0]],
    'plasticity': [3, ['PrandtlRaussCorrector']],
    'matrixDecomposition': [3, ['analytical']], 
    'bodies': [2, []], 'body': [3, ['cube']],
    'mesh': [4, ['main', 'geo2', 'models/cube.geo', 0.2]], 
    'material': [4, ['steel']],
    'borderCondition': [2, ['ExternalForceCalculator', -2160, 0.0]], 
    'area': [3, ['box', -10, 10, -10, 10, 4.9, 5.1]]}

    make_xml(tags, 'testing_xml')