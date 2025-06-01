def send(s):
    binary_string = ''.join(format(ord(c), '07b') for c in s) 
    encoded_message = ""
    current_bit = None
    count = 0

    for bit in binary_string:
        if bit == current_bit:
            count += 1
        else:
            if current_bit is not None:
                encoded_message += ("00 " if current_bit == '0' else "0 ") + "0" * count + " "
            current_bit = bit
            count = 1

    if current_bit is not None: 
        encoded_message += ("00 " if current_bit == '0' else "0 ") + "0" * count
    return encoded_message.strip()  


def receive(s):
    blocks = s.split()
    binary_string = ""
    i = 0
    while i < len(blocks):
        first_block = blocks[i]
        second_block = blocks[i+1]
        bit = '1' if first_block == "0" else '0'
        count = len(second_block)
        binary_string += bit * count
        i += 2
    
    decoded_string = ""
    for i in range(0, len(binary_string), 7):
        byte = binary_string[i:i+7]
        decoded_string += chr(int(byte, 2))
    return decoded_string