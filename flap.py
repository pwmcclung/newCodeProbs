ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"

def flap_display(lines, rotors):
    result = []
    for i, line in enumerate(lines):
        new_line = ""
        rotor_moves = rotors[i]
        for j, char in enumerate(line):
            rotor_index = ALPHABET.index(char)
            total_moves = sum(rotor_moves[:j+1])
            new_rotor_index = (rotor_index + total_moves) % len(ALPHABET)
            new_line += ALPHABET[new_rotor_index]
        result.append(new_line)
    return result