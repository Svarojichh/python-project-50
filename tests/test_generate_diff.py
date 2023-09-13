from gendiff.work_fold.folder import generate_diff
import pytest


def read(result_txt):
    with open(result_txt, 'r') as text:
        result = text.read()
    return result


def file_path(file):
    path = 'tests/fixtures/'
    path_constructor = f'{path}{file}'
    return path_constructor


assert generate_diff(file_path('file1.json'), file_path('file2.json')) == read(file_path('json_result.txt'))
