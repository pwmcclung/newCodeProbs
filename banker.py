def fortune(f0, p, c0, n, i):
    p /= 100  
    i /= 100  

    fn = f0
    cn = c0

    for _ in range(1, n):
        fn = int(fn + fn * p - cn)  
        cn = int(cn + cn * i) 

        if fn < 0:  
            return False

    return True
