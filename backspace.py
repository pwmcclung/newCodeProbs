def solve(s):
    # 1. Initialize an empty list to store typed characters. This list acts as our "stack."
    result = []
    # 2. Initialize a pointer 'i' to the beginning of the string 's'
    i = 0
    # 3. Loop through the string 's' using the pointer 'i' until the end of the string
    while i < len(s):
        # 4. Check if the current character at 'i' is '[' and if the next 9 chars matches 'backspace'
        if s[i] == '[' and s[i+1:i+10] == 'backspace':
            # 5. Check if a multiple backspace is used ie [backspace]*n
            if i + 11 < len(s) and s[i+11] == '*':
                # 6. If it is, initialize pointer 'j' to move through the digit
                j = i + 12
                 # 7. Use pointer 'j' to move through and extract the number
                while j < len(s) and s[j].isdigit():
                    j += 1
                # 8. Extract number of backspaces by slicing s
                num_backspaces = int(s[i + 12:j])
                # 9. Loop through the number of backspaces
                for _ in range(num_backspaces):
                    # 10. If there are characters in result, remove them
                    if result:
                        result.pop()
                # 11. Move pointer i to after the number of backspaces
                i = j
            # 12. If the above case was not true, then its a single backspace
            else:
                # 13. check if there is a previous character in list
                if result:
                    # 14. if so, remove last character
                    result.pop()
                # 15. increase i by 11 to skip over [backspace]
                i += 11

        # 16. If the character is not '[' then it must be a regular character
        else:
            # 17. Append character to list
            result.append(s[i])
            # 18. Increase the pointer by one
            i += 1
    # 19. After the while loop, join the list into a string and return
    return "".join(result)
