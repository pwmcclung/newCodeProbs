from datetime import datetime, timedelta, date

def gigasecond(start_date):
    days_to_add = 11574
    date_object = datetime.strptime(str(start_date), "%Y-%m-%d")
    new_date = date_object + timedelta(days=days_to_add)
    return date(new_date.year,new_date.month,new_date.day)
