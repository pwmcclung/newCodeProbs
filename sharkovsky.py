def s_vs(n):
        k = 0
        while n % 2 == 0 and n > 0:
            n //= 2
            k += 1

        if n == 1 and k > 0:  
            return (2, 0, k)
        elif n % 2 != 0:  
            return (1, n, k)
        else:
            return(0, 0, 0)

def sharkovsky(a, b):
    
    if a == b:
        return False
    if a == 1:
        return False
    if b == 1:
        return True
        
    a_val = s_vs(a)
    b_val = s_vs(b)

    if a_val[0] == 1 and b_val[0] == 1: 
        if a_val[2] == b_val[2]:
            return a_val[1] < b_val[1]
        else:
            return a_val[2] < b_val[2]
    elif a_val[0] == 1 and b_val[0] == 2: 
        return True
    elif a_val[0] == 2 and b_val[0] == 1:  
        return False
    elif a_val[0] == 2 and b_val[0] == 2: 
        return a_val[2] > b_val[2]
    else:
        return False