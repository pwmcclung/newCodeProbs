def largest_power(N):
    k = -1
    power_value = 1  
    while power_value < N:
        k += 1  
        power_value *= 3
    return k
   
