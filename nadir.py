def recurrence(values):
    nadir = min(values)
    nadir_index = values.index(nadir)

    after_nadir = values[nadir_index:]

    if len(after_nadir) < 4:
        return False

    count = 0
    for i in range(1, len(after_nadir)):
        if after_nadir[i] > after_nadir[i-1]:
            count += 1
            if count >= 3:
                return True
        else:
            count = 0       
    return False