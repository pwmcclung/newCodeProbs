import numpy as np
def manhattan_distance(pointA, pointB):
    point_a = np.array(pointA)
    point_b = np.array(pointB)
    distance = np.sum(np.abs(point_a - point_b))
    return distance
