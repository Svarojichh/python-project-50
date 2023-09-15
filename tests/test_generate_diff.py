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


def test_generate_diff():
    assert generate_diff(file_path('file1.json'), file_path('file2.json')) == read(file_path('results.txt'))
    assert generate_diff(file_path('filepath1.yml'), file_path('filepath2.yml')) == read(file_path('results.txt'))
