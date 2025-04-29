def on_line(points):
    n = len(points)
    if n <= 2:
        return True

    p1 = points[0]
    x1, y1 = p1

    p2 = None
    first_diff_index = -1
    for i in range(1, n):
        if points[i] != p1:
            p2 = points[i]
            first_diff_index = i
            break

    if p2 is None:
        return True

    x2, y2 = p2

    ref_dx = x2 - x1
    ref_dy = y2 - y1


    for i in range(1, n): 
        pi = points[i]
        xi, yi = pi

        curr_dx = xi - x1
        curr_dy = yi - y1

        if ref_dy * curr_dx != curr_dy * ref_dx:
            return False

    return True
