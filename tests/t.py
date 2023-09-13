from gendiff.work_fold.folder import generate_diff
import pytest


def read(result_txt):
    with open(result_txt, 'r') as text:
        result = text.read()
    return result

def file_path():
    path = 'fixtures/'
    def inner(file):
        path_constructor = f'{path}{file}'
        return path_constructor
    return inner


PATH = file_path()

print(generate_diff(PATH('file1.json'), PATH('file2.json')))
print(read(PATH('json_result.txt')))
print(generate_diff('fixtures/file1.json', 'fixtures/file2.json'))

