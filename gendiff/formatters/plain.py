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


def get_plain_format(current_data, property_path=''):
    lines = []
    keys_iter = iter(current_data.items())
    for key, value in keys_iter:
        current_value1 = format_values(value)
        if ('(remote)' in key
                and f'{key.removesuffix("(remote)")}(added)'
                in current_data.keys()):
            key, value = next(keys_iter)
            current_value2 = format_values(value)
            key = key.removesuffix("(added)")
            lines.append(f"Property '{property_path}{key}' was updated. "
                         f"From {current_value1} to {current_value2}")
        elif '(remote)' in key:
            key = key.removesuffix("(remote)")
            lines.append(f"Property '{property_path}{key}' was removed")
        elif '(added)' in key:
            key = key.removesuffix("(added)")
            lines.append(f"Property '{property_path}{key}' "
                         f"was added with value: {current_value1}")
        elif current_value1 == '[complex value]':
            new_property_path = property_path + key + '.'
            lines.append(f'{get_plain_format(value, new_property_path)}')
    return '\n'.join(lines)
