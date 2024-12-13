def score_throws(radii):
    if len(radii) == 0:
        return 0
    points = 0
    ten_count = 0
    for x in range(len(radii)):
        floated = float(radii[x])
        if floated <= 4.99:
            points += 10
            ten_count += 1
        elif floated <= 10.00 and floated >= 5.00:
            points += 5
        else:
            points += 0
    if ten_count == len(radii):
        return points + 100
    else:
        return points