#!/usr/bin/env python3

from gendiff.parser import arg_parser
from gendiff.work_fold.folder import generate_diff


def main():
    first_file, second_file = arg_parser()
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
