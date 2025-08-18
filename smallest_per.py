def minimum_percentage(foods):
    if not foods:
        return 100
    sum_of_percents = sum(foods)
    minimum = sum_of_percents - (len(foods) - 1) * 100
    return max(0, minimum)