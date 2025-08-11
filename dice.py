import random
def throw_rigged():
    if random.random() < 0.22:
        return 6
    else:
        return random.randint(1,5)