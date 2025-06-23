      
def hex_string_to_RGB(hex_string):

    # STEP 1: INPUT VALIDATION

    if not hex_string.startswith("#"): #Check if the string starts with '#'
        return None #Return None if input does not follow hexadecimal format.
    if len(hex_string) != 7: #Check if the string length is correct (including '#').
        return None #Return None if input does not follow hexadecimal format.

    hex_string = hex_string.lower() #Convert to lowercase for case-insensitive comparison.


    # STEP 2: EXTRACT HEX VALUES FOR R, G, B

    r_hex = hex_string[1:3]  #Extract the hex code for the red component (positions 1-2)
    g_hex = hex_string[3:5]  #Extract the hex code for the green component (positions 3-4)
    b_hex = hex_string[5:7]  #Extract the hex code for the blue component (positions 5-6)

    # STEP 3: CONVERT HEX STRINGS TO INTEGERS

    try:
        r = int(r_hex, 16)  #Convert the red hex string to an integer using base 16
        g = int(g_hex, 16)  #Convert the green hex string to an integer using base 16
        b = int(b_hex, 16)  #Convert the blue hex string to an integer using base 16
    except ValueError:
        return None #Return None if any hex string is not a valid hex number.


    # STEP 4: CREATE AND RETURN THE RGB DICTIONARY
    return {"r": r, "g": g, "b": b} #Create and return the dictionary with RGB values