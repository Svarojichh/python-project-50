import itertools


def get_stylish_format(current_data, depth=0):
    replacer = ' '
    spaces_count = 4
    lines = []

    if not isinstance(current_data, dict):
        if current_data is None:
            return 'null'
        if isinstance(current_data, str):
            return current_data
        return str(current_data).lower()

    deep_indent_size = depth + spaces_count
    current_indent = replacer * depth
    for key, value in current_data.items():
        if key.endswith('(remote)'):
            deep_indent = replacer * (deep_indent_size - 2)
            key_output = f'- {key.removesuffix("(remote)")}'
        elif key.endswith('(added)'):
            deep_indent = replacer * (deep_indent_size - 2)
            key_output = f'+ {key.removesuffix("(added)")}'
        else:
            deep_indent = replacer * deep_indent_size
            key_output = key
        lines.append(f'{deep_indent}{key_output}:'
                     f' {get_stylish_format(value, deep_indent_size)}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
