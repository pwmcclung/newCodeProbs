import datetime

def most_frequent_days(year):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_counts = {day: 0 for day in days}

    for month in range(1, 13):
        for day in range(1, 32):  
            try:
                date = datetime.date(year, month, day)
                day_of_week = date.strftime("%A")  
                day_counts[day_of_week] += 1
            except ValueError:
                pass  

    max_count = max(day_counts.values())
    most_frequent = [day for day, count in day_counts.items() if count == max_count]
    most_frequent.sort(key=lambda x: days.index(x)) 

    return most_frequent