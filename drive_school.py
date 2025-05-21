def cost(mins):
    if mins < 66:
        return 30
    else:
        cost = 30
        minS = mins - 60
        count = 0
        while minS > 5:
            count += 1
            minS -= 30
        if minS <=5:
            return cost + (count * 10)