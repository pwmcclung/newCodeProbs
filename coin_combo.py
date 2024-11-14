def coin_combo(cents):
    pennies = 0
    nickels = 0
    dimes = 0
    quarters = 0
    change_needed = cents
    while change_needed  != 0:
        if change_needed > 24:
            while change_needed  > 24:
                quarters += 1
                change_needed  -= 25
        if change_needed  > 9:
            while change_needed > 9:
                dimes += 1
                change_needed-= 10
        if change_needed > 4:
            while change_needed > 4:
                nickels += 1
                change_needed -= 5
        if change_needed < 5:
            while change_needed > 0:
                pennies += 1
                change_needed -= 1
    return [pennies, nickels, dimes, quarters]