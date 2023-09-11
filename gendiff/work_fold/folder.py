from json import load


def generate_diff(file1, file2):
    f1 = load(open(file1))
    f2 = load(open(file2))
    result = {}
    for key1, value1 in f1.items():
        for key2, value2 in f2.items():
            if key1 == key2 and value1 == value2:
                result[f'  {key1}'] = value1
            elif key1 == key2 and value1 != value2:
                result[f'- {key1}'] = value1
                result[f'+ {key2}'] = value2
            if key2 not in f1:
                result[f'+ {key2}'] = value2
        if key1 not in f2:
            result[f'- {key1}'] = value1
    sorted_result = dict(sorted(result.items(), key=lambda x: x[0][2:]))
    lines = ["{\n", '\n'.join((f'  {key}: {value}' for key, value in sorted_result.items())), "\n}"]
    out_text = ''.join(lines)
    return out_text







