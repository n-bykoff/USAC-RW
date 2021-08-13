import json


def write_to_json_file(json_data, file_name):
    with open(f'{file_name}.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=6)
        json_file.close()


def read_from_json(file_name):
    with open(f'{file_name}.json') as json_file:
        json_object = json.load(json_file)
        json_file.close()

    return json_object
