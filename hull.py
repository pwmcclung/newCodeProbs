def hull_method(pointlist):

    pointlist = list({tuple(p) for p in pointlist}) 

    if len(pointlist) < 3:
        return pointlist 


    start_point = min(pointlist, key=lambda p: (p[1], p[0]))
    hull = [list(start_point)] 
    endpoint = start_point

    while True:
        next_point = pointlist[0]  
        for p in pointlist:
            if p == endpoint:
                continue

            cross_product = cross_product_2d(endpoint, next_point, p)
            if cross_product > 0 or cross_product == 0 and dist_sq(endpoint, p) > dist_sq(endpoint, next_point):
                next_point = p

        if next_point == start_point:
            break

        hull.append(list(next_point)) 
        endpoint = next_point

    return hull

def cross_product_2d(o, a, b):
    
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dist_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2