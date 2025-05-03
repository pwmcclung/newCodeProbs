import math

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

def summation_of_primes(primes):
    sum = 0
    num = 0
    while num <= primes:
        if is_prime(num):
            sum += num
        num += 1
    return sum
