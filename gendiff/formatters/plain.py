def format_values(value):
    if not isinstance(value, dict):
        if value is None:
            result_value = 'null'
        elif isinstance(value, str):
            result_value = f"'{value}'"
        else:
            result_value = str(value).lower()
    else:
        result_value = '[complex value]'
    return result_value


def get_plain_format(data, path=''):
    lines = []
    iter_keys = iter(data.items())
    for key, value in iter_keys:
        current_value = format_values(value)
        if ('(remote)' in key
                and f'{key.removesuffix("(remote)")}(added)'
                in data.keys()):
            key, value = next(iter_keys)
            current_value1 = format_values(value)
            key = key.removesuffix("(added)")
            lines.append(f"Property '{path}{key}' was updated. "
                         f"From {current_value} to {current_value1}")
        elif '(remote)' in key:
            key = key.removesuffix("(remote)")
            lines.append(f"Property '{path}{key}' was removed")
        elif '(added)' in key:
            key = key.removesuffix("(added)")
            lines.append(f"Property '{path}{key}' "
                         f"was added with value: {current_value}")
        elif current_value == '[complex value]':
            new_property_path = path + key + '.'
            lines.append(f'{get_plain_format(value, new_property_path)}')
    return '\n'.join(lines)
