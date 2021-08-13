from json_module import read_from_json


def change_tag_string(line, text_or_property, property_name, new_value):
    if text_or_property == 'property':
        line_list = line.split(property_name)
        line = line_list[0] + f'{property_name}="{new_value}" ' + '" '.join(line_list[1].split('" ')[1:])
    elif text_or_property == 'text':
        line_list = line.split('>')
        line = line_list[0] + f'>{new_value}<' + line_list[1].split('<')[1] + '>'

    return line


def replace_tag_value(lines, tag, text_or_property, property_name, new_value, line_index):
    tag_counter = 0
    indexes = []

    for i, line in enumerate(lines):
        if f'<{tag}' in line and f'{property_name}=' in line:
            tag_counter += 1
            indexes.append(i)
        elif f'<{tag}>' in line and property_name == '':
            tag_counter += 1
            indexes.append(i)

    if tag_counter == 0:
        print("We haven't this tag or this tag haven't this property\nPlease start again")
        return lines

    print(tag, indexes)

    if tag_counter == 1:
        line = lines[indexes[0]]
        new_line = change_tag_string(line, text_or_property, property_name, new_value)
        lines[indexes[0]] = new_line

    elif tag_counter > 1:
        index = indexes.index(line_index - 1)
        line = lines[indexes[index]]

        new_line = change_tag_string(line, text_or_property, property_name, new_value)
        lines[indexes[index]] = new_line

    return lines


def replace_tag_value_from_json(lines, json_name):
    params = read_from_json(json_name)
    print(params)

    tag = list(params.keys())[0]

    for i in range(len(params[tag][-1])):
        name = ''
        for tag in params.keys():

            print(params[tag])
            text_or_property = params[tag][0]

            if text_or_property == 'text':
                property_name = ''
                new_values_series = params[tag][1]
                new_value = new_values_series[i]
                index = params[tag][2][i]
                name += f'{tag}_{new_value}_'
            elif text_or_property == 'property':
                property_name = params[tag][1]
                new_values_series = params[tag][2]
                new_value = new_values_series[i]
                index = params[tag][3][i]
                name += f'{property_name}_{new_value}_'
            else:
                return lines

            lines = replace_tag_value(lines, tag, text_or_property, property_name, new_value, index)

        with open(f'./templates/template_{name[:-1]}.xml', 'w') as f:
            for line in lines:
                f.write(line)

    return lines