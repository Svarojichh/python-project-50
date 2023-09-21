import json
import yaml


def get_dict_from_files(file):
    if file.endswith('.json'):
        with open(file) as file:
            return json.load(file)
    elif file.endswith('.yml') or file.endswith('.yaml'):
        with open(file) as file:
            return yaml.safe_load(file)
