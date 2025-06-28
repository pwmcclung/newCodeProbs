def travel(total_time, run_time, rest_time, speed):
    if total_time == 0 or run_time == 0 or speed == 0:
        return 0
    elif rest_time == 0:
        intervals = (total_time / run_time)
        return intervals * (run_time * speed)
    run = 0
    left_over = 0
    if total_time > run_time + rest_time:
        while total_time > run_time + rest_time:
            run += run_time * speed
            total_time -= run_time + rest_time
        if total_time <= run_time:
            left_over += total_time * speed
        elif total_time > run_time and total_time < run_time+rest_time:
            left_over += run_time * speed
        return run + left_over
    elif total_time < run_time:
        return (run_time * speed)* (total_time / run_time)