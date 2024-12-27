def deficiently_abundant_amicable_numbers(n1, n2):
    n1_sum = sum(getDivs(n1)[0:-1])
    n2_sum = sum(getDivs(n2)[0:-1])
    
    whats_first = ''
    if n1_sum > n1:
        whats_first = 'abundant'
    elif n1_sum < n1:
        whats_first = 'deficient'
    else:
        whats_first = 'perfect'
    
    whats_second = ''
    if n2_sum > n2:
        whats_second = 'abundant'
    elif n2_sum < n2:
        whats_second = 'deficient'
    else:
        whats_second = 'perfect'
        
    ami = ''
    if n1 == n2:
        ami = 'not amicable'
    elif n2_sum == n1 and n1_sum == n2 and n1 != n2:
        ami = 'amicable'
    else:
        ami = 'not amicable'

    return whats_first + ' ' + whats_second + ' ' + ami
    
def getDivs(N):
    factors = {1}
    maxP  = int(N**0.5)
    p,inc = 2,1
    while p <= maxP:
        while N%p==0:
            factors.update([f*p for f in factors])
            N //= p
            maxP = int(N**0.5)
        p,inc = p+inc,2
    if N>1:
        factors.update([f*N for f in factors])
    return sorted(factors)