import json
import yaml


def parse_data(content, format_file):
    if format_file == 'json':
        return json.loads(content)
    elif format_file in ['yml', 'yaml']:
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported file format: {format_file}")


def read_data(data):
    with open(data) as open_data:
        return open_data.read()


def get_format_file(path):
    format_file = path.split(".")[-1]
    return format_file
