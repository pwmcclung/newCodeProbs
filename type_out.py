def type_out(s):

    result = []  # Store the result as a list of characters for easy concatenation
    copied_text = ""  # Store the copied text
    i = 0  # Initialize a pointer to iterate through the input string

    while i < len(s):
        if s[i] == '[': # Check if we found a bracket
            j = i + 1 # Move a pointer to the start of the content
            while j < len(s) and s[j] != ']':
                j += 1 # Move the pointer to the end bracket

            command = s[i + 1:j] # Get the command in between brackets

            if command.isdigit(): # If number paste copied text number times
                num_repeats = int(command)
                result.append(copied_text * num_repeats)
            elif command: # If text copy, then paste
                copied_text = command
                result.append(copied_text)
            else: # if empty then paste
                result.append(copied_text)
            i = j + 1 # Move the index after the closing bracket

        else:
          result.append(s[i]) # Regular char
          i += 1
    return "".join(result) # convert the char list to a string