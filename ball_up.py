def max_ball(v0):
    g = 9.81  
    v0 = v0 * 1000 / 3600  

    t_max = v0 / g 

    t_max_tenths = int(round(t_max * 10))

    return t_max_tenths