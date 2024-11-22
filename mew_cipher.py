import re
def decipher(code):
    num_strings = len(code)
    string_length = len(code[0])
    decoded_string = ""
    for i in range(string_length):
        char_sum = 0
        for s in code:
            char = s[i]
            if 'a' <= char <= 'z':
                char_sum += ord(char) - ord('a') + 1
            elif char == ' ':
                char_sum += 0

        average = char_sum / num_strings if num_strings >0 else 0 

        decoded_char = chr(ord('a') + int(average) -1) if average > 0 else ' '
        decoded_string += decoded_char
    new_str = re.sub('`', ' ', decoded_string)
    return new_str