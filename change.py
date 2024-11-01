def give_change(amount): 
    
    ones = 0
    fives = 0
    tens = 0
    twenties = 0
    fifties = 0
    hundreds = 0
    
    new_amt = amount 
    
    while new_amt > 0:
        if new_amt > 99:
            while new_amt > 99:
                hundreds += 1
                new_amt -= 100
        if new_amt > 49  and new_amt < 100:
            while new_amt > 49 and new_amt < 100:
                fifties += 1
                new_amt -= 50
        if new_amt >19 and new_amt < 50:
            while new_amt > 19 and new_amt < 50:
                twenties += 1
                new_amt -= 20
        if new_amt >9 and new_amt < 20:
            while new_amt > 9 and new_amt < 20:
                tens += 1
                new_amt -= 10
        if new_amt >4 and new_amt < 10:
            while new_amt > 4 and new_amt < 10:
                fives += 1
                new_amt -= 5
        if new_amt > 0 and new_amt < 6:
            while new_amt > 0 and new_amt <6:
                ones += 1
                new_amt -= 1
                
    return (ones, fives, tens, twenties, fifties, hundreds)