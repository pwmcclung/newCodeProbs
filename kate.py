def has_exit(maze):
    row_count = len(maze)
    kates_positions = []
    for r in range(row_count):
        cols = len(maze[r])
        for c in range(cols):
            if maze[r][c] == 'k':
                kates_positions.append((r, c))
    if len(kates_positions) != 1:
        raise ValueError
    kates_row, kates_col = kates_positions[0]
    visited = set()
    def kate_checker(row, col):
        if (row, col) in visited:
            return False
        visited.add((row, col))
        if row < 0 or row >= row_count or col < 0 or col >= len(maze[row]):
            return True
        if maze[row][col] == '#':
            return False
        return (kate_checker(row + 1, col) or  
                kate_checker(row - 1, col) or  
                kate_checker(row, col + 1) or  
                kate_checker(row, col - 1))    
    return kate_checker(kates_row, kates_col)