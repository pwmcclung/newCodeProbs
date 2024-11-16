def was_package_received_yesterday(tz_from, tz_to, start, duration):
    hour_diff = (tz_from - tz_to) 
    time_calc = (start - hour_diff)+ duration
    if tz_from <= tz_to:
        return False
    if tz_to < tz_from: 
        if time_calc >= 0:
            return False
        elif time_calc < 0:
            return True