def howmuch(m, n):
    results = []
    for f in range(min(m,n), max(m,n) + 1):
        if (f - 1) % 9 == 0:
            c = (f - 1) // 9
            if (f - 2) % 7 == 0:
                b = (f - 2) // 7
                results.append(["M: " + str(f), "B: " + str(b), "C: " + str(c)])
    return results