def doubles(s):
    no_dubs = []
    for char in s:
        if no_dubs and no_dubs[-1] == char:
            no_dubs.pop()
        else:
            no_dubs.append(char)
    return "".join(no_dubs)