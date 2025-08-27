def stat(strg):
    if not strg:
        return ""

    times = []
    for time_str in strg.split(','):
        h, m, s = map(int, time_str.strip().split('|'))
        times.append(h * 3600 + m * 60 + s)

    times.sort()
    n = len(times)

    rng = times[-1] - times[0]
    avg = sum(times) // n
    median = times[n // 2] if n % 2 else (times[n // 2 - 1] + times[n // 2]) // 2

    def format_time(seconds):
        h = seconds // 3600
        seconds %= 3600
        m = seconds // 60
        s = seconds % 60
        return f"{h:02}|{m:02}|{s:02}"

    return f"Range: {format_time(rng)} Average: {format_time(avg)} Median: {format_time(median)}"