import json
import yaml


def get_dict_from_files(file):
    if file.endswith('.json'):
        return json.load(open(file))
    elif file.endswith('.yml') or file.endswith('.yaml'):
        return yaml.safe_load(open(file))
