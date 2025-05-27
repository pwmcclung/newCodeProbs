def name_in_str(strng : str, name : str) -> bool:
    strng = strng.lower()
    name = name.lower()
    
    i = 0
    j = 0
    while i < len(strng) and j < len(name):
        if strng[i] == name[j]:
            j += 1
        i += 1
    return j == len(name)