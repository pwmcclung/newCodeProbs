def is_interesting(number, awesome_phrases):
    number_str = str(number)
    if number < 100:
        if any(is_interesting_number(number + i, awesome_phrases) for i in range(1, 3)):
            return 1  
        else:
            return 0

    if is_interesting_number(number, awesome_phrases):
        return 2
    elif any(is_interesting_number(number + i, awesome_phrases) for i in range(1, 3)):
        return 1
    else:
        return 0

    

def is_interesting_number(number, awesome_phrases):
    number_str = str(number)
    if len(number_str) < 3:
        return False

    if number in awesome_phrases:
        return True
    if all(c == '0' for c in number_str[1:]):  
        return True
    if all(c == number_str[0] for c in number_str): 
        return True
    if is_sequential(number_str, 1):  
        return True
    if is_sequential(number_str, -1): 
        return True
    if number_str == number_str[::-1]:  
        return True

    return False

def is_sequential(number_str, step):
    for i in range(len(number_str) - 1):
        prev = int(number_str[i])
        curr = int(number_str[i+1])
        if (curr - prev) != step:
            if step == 1 and prev == 9 and curr == 0:
                continue
            elif step == -1 and prev == 1 and curr == 0:
                continue
            else: return False
    return True