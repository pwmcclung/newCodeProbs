def plant(seed, water, fert, temp):
    if temp < 31 and temp > 19:
        return ('-' * water + seed*fert)* water
    else:
        return (('-' * water)* water) + seed
