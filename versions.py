def compare_versions(version1,version2):
    v1_parts = [int(x) for x in version1.split('.')]
    v2_parts = [int(x) for x in version2.split('.')]

    max_len = max(len(v1_parts), len(v2_parts))

    v1_parts += [0] * (max_len - len(v1_parts))
    v2_parts += [0] * (max_len - len(v2_parts))

    for i in range(max_len):
        if v1_parts[i] > v2_parts[i]:
            return True
        elif v1_parts[i] < v2_parts[i]:
            return False

    return True