from gendiff.work_fold.generator import gen_diff
from gendiff.formatters.stylish import get_stylish_format
from gendiff.parser import arg_parser
from gendiff.work_fold.open_files import get_dict_from_files
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json import get_json_format


def generate_diff(file1, file2, type_format='stylish'):
    file1_data = get_dict_from_files(file1)
    file2_data = get_dict_from_files(file2)
    result_dict_from_gen_diff = gen_diff(file1_data, file2_data)
    if type_format == 'stylish':
        return get_stylish_format(result_dict_from_gen_diff)
    elif type_format == 'plain':
        return get_plain_format(result_dict_from_gen_diff)
    elif type_format == 'json':
        return get_json_format(result_dict_from_gen_diff)


def result_output():
    first_file, second_file, format_type = arg_parser()
    return print(generate_diff(first_file, second_file, format_type))
