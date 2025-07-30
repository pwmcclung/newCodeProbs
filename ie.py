def i_before_e(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i] in ('i', 'e'):
            start = i
            count_i = 0
            count_e = 0
            while i < len(s) and s[i] in ('i', 'e'):
                if s[i] == 'i':
                    count_i += 1
                else:
                    count_e += 1
                i += 1

            if start > 0 and s[start - 1] == 'c':
                result += 'e' * count_e + 'i' * count_i
            else:
                result += 'i' * count_i + 'e' * count_e
        else:
            result += s[i]
            i += 1

    return result