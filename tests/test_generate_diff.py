from gendiff.work_fold.folder import gen_diff, get_sorted_keys_from_files
from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.json import get_json_format
from gendiff.work_fold.open_files import get_dict_from_files
import pytest


def read(result_txt):
    with open(result_txt, 'r') as text:
        result = text.read()
    return result


def file_path(file):
    path = 'tests/fixtures/'
    path_constructor = f'{path}{file}'
    return path_constructor


file1_data_json = get_dict_from_files(file_path('file1.json'))
file2_data_json = get_dict_from_files(file_path('file2.json'))
file1_data_yml = get_dict_from_files(file_path('filepath1.yml'))
file2_data_yml = get_dict_from_files(file_path('filepath2.yml'))

result_dict_gen_diff_json = gen_diff(file1_data_json, file2_data_json)
result_dict_gen_diff_yml = gen_diff(file1_data_yml, file2_data_yml)


@pytest.fixture
def result_output_from_files():
    return {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True,
                       'setting6': {'key': 'value', 'doge': {'wow': ''}}},
            'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
            'group2': {'abc': 12345, 'deep': {'id': 45}}}


@pytest.fixture
def result_dict_from_generate_diff():
    return {'common': {'follow(added)': False, 'setting1': 'Value 1', 'setting2(remote)': 200, 'setting3(remote)': True,
                       'setting3(added)': None, 'setting4(added)': 'blah blah', 'setting5(added)': {'key5': 'value5'},
                       'setting6': {'doge': {'wow(remote)': '', 'wow(added)': 'so much'}, 'key': 'value',
                                    'ops(added)': 'vops'}},
            'group1': {'baz(remote)': 'bas', 'baz(added)': 'bars', 'foo': 'bar', 'nest(remote)': {'key': 'value'},
                       'nest(added)': 'str'}, 'group2(remote)': {'abc': 12345, 'deep': {'id': 45}},
            'group3(added)': {'deep': {'id': {'number': 45}}, 'fee': 100500}}


@pytest.fixture
def result_keys_for_files():
    return ['common', 'group1', 'group2', 'group3']


def test_get_stylish_format():
    assert get_stylish_format(result_dict_gen_diff_json) == read(file_path('results.txt'))
    assert get_stylish_format(result_dict_gen_diff_yml) == read(file_path('results.txt'))


def test_get_plain_format():
    assert get_plain_format(result_dict_gen_diff_json) == read(file_path('result_plain.txt'))
    assert get_plain_format(result_dict_gen_diff_yml) == read(file_path('result_plain.txt'))


def test_get_json_format():
    assert get_json_format(result_dict_gen_diff_json) == read(file_path('result_json.txt'))
    assert get_json_format(result_dict_gen_diff_yml) == read(file_path('result_json.txt'))


def test_gen_diff(result_dict_from_generate_diff):
    assert result_dict_gen_diff_json == result_dict_from_generate_diff
    assert result_dict_gen_diff_yml == result_dict_from_generate_diff


def test_get_sorted_keys_from_files(result_keys_for_files):
    assert get_sorted_keys_from_files(file1_data_json, file2_data_json) == result_keys_for_files
    assert get_sorted_keys_from_files(file1_data_yml, file2_data_yml) == result_keys_for_files


def test_get_dict_from_files(result_output_from_files):
    assert file1_data_json == result_output_from_files
    assert file1_data_yml == result_output_from_files
