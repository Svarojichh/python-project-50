def get_sorted_keys_from_files(dict_file1, dict_file2):
    sorted_key = sorted(set(dict_file1) | set(dict_file2))
    return sorted_key


def generate_diff(dict_file1, dict_file2):
    result_diff = {}
    sorted_keys_from_files = get_sorted_keys_from_files(dict_file1, dict_file2)
    for key in sorted_keys_from_files:
        if (key in dict_file1 and key in dict_file2
                and dict_file1[key] == dict_file2[key]):
            result_diff[key] = dict_file1[key]
        elif key not in dict_file2:
            result_diff[f'{key}(remote)'] = dict_file1[key]
        elif key not in dict_file1:
            result_diff[f'{key}(added)'] = dict_file2[key]
        elif (isinstance(dict_file1[key], dict)
              and isinstance(dict_file2[key], dict)):
            result_diff[key] = generate_diff(dict_file1[key], dict_file2[key])
        elif dict_file1[key] != dict_file2[key]:
            result_diff[f'{key}(remote)'] = dict_file1[key]
            result_diff[f'{key}(added)'] = dict_file2[key]
    return result_diff
