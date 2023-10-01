#!/usr/bin/env python3

from gendiff.main import generate_diff
from gendiff.cli import arg_parser


def main():
    first_file, second_file, format_type = arg_parser()
    return print(generate_diff(first_file, second_file, format_type))


if __name__ == '__main__':
    main()
