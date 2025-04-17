import math

def calc_tip(p, r):

    # Round the price at the tens place
    if p % 10 == 0:
        rounded_price = p
    else:
        rounded_price = (p // 10) * 10
        if p % 10 >4:
            rounded_price += 10
        
        if p < 5:
            rounded_price = 0 

    # Calculate the base tip
    base_tip = rounded_price // 10

    # Apply the satisfaction rating
    if r == 1:
        tip = base_tip + 1
    elif r == 0:
        tip = base_tip - 1
    else:
        tip = (base_tip // 2) - 1

    # Ensure the tip is non-negative
    return max(0, tip)