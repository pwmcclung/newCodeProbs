def cartesian_neighbor(x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0: 
                continue
            neighbors.append((x + dx, y + dy))
    return neighbors