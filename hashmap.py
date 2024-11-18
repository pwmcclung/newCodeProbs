from collections import defaultdict
def my_hash_map(list_of_strings):
    new_dict = defaultdict(list)
    for x in range(len(list_of_strings)):
        new_dict[ascii_val(list_of_strings[x])].append(list_of_strings[x])
    return new_dict
    
def ascii_val(word):
    return sum(ord(char) for char in word)