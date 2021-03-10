class Tag:
    def __init__(self, name, *args):
        self.name = name
        self.params = args

    def create_string(self):
        params = self.params

        if self.name == 'task':
            string = f'<task numberOfSnaps="{params[0]}" stepsPerSnap="{params[1]}">\n</task>'
            return string
        elif self.name == 'system':
            string = f'\t<system>\n\t\t<meshMovement type="{params[0]}" />' +\
            f'\n\t\t<timeStep multiplier="{params[1]}" />' +\
            f'\n\t\t<plasticity type="{params[2]}" />' +\
            f'\n\t\t<matrixDecomposition implementation="{params[3]}" />' +\
            '\n\t</system>'
            return string
        elif self.name == 'bodies':
            string = f'\t<bodies>\n\t\t<body id="{params[0]}">' +\
            f'\n\t\t\t<mesh id="{params[1]}" type="{params[2]}" ' +\
            f'file="{params[3]}" tetrSize="{params[4]}" />' +\
            f'\n\t\t\t<material id="{params[5]}" />' +\
            '\n\t\t</body>\n\t</bodies>'
            return string


def make_xml():
    task = Tag('task', 150, 1)
    task_string = task.create_string()

    system = Tag('system', 'none', 1.0, 'PrandtlRaussCorrector', 'analytical')
    sys_string = system.create_string()

    bodies = Tag('bodies', 'cube', 'main', 'geo2', 'models/cube.geo',
        0.2, 'steel')
    bodies_string = bodies.create_string()

    string = task_string.replace('\n', f'\n{sys_string}\n{bodies_string}\n')
    return string


if __name__ == '__main__':
    print(make_xml())