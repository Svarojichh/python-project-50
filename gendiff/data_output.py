from gendiff.work_fold.folder import generate_diff
from gendiff.formatters.stylish import get_stylish_format
from gendiff.parser import arg_parser
from gendiff.work_fold.open_files import get_dict_from_files
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json import get_json_format


first_file, second_file, format_type = arg_parser()
file1_data = get_dict_from_files(first_file)
file2_data = get_dict_from_files(second_file)


def gen_diff(file1, file2, type_format):
    result_dict_from_generate_diff = generate_diff(file1, file2)
    if type_format == 'stylish':
        return get_stylish_format(result_dict_from_generate_diff)
    elif type_format == 'plain':
        return get_plain_format(result_dict_from_generate_diff)
    elif type_format == 'json':
        return get_json_format(result_dict_from_generate_diff)


def result_output():
    return print(gen_diff(file1_data, file2_data, format_type))
