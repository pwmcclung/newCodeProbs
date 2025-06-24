import re
def whitespace(string):
    return re.fullmatch(r"^\s*$", string) is not None