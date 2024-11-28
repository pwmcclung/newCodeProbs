def days_represented(trips):
    all_days = [0] * 366  

    for arrival, departure in trips:
        for day in range(arrival, departure +1):
            all_days[day-1] = 1  

    return sum(all_days)