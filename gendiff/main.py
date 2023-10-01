from gendiff.generator import gen_diff
from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json import get_json_format
from gendiff.parser import parse_data, get_format_file, read_data


def generate_diff(file1, file2, type_format='stylish'):
    file1_data = parse_data(read_data(file1), get_format_file(file1))
    file2_data = parse_data(read_data(file2), get_format_file(file2))
    result_dict_from_gen_diff = gen_diff(file1_data, file2_data)
    if type_format == 'stylish':
        return get_stylish_format(result_dict_from_gen_diff)
    elif type_format == 'plain':
        return get_plain_format(result_dict_from_gen_diff)
    elif type_format == 'json':
        return get_json_format(result_dict_from_gen_diff)
