def find_word(board, word):
    rows = len(board)
    cols = len(board[0])

    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def dfs(row, col, word_index, visited):
        if word_index == len(word):
            return True

        if not is_valid(row, col) or (row, col) in visited or board[row][col] != word[word_index]:
            return False

        visited.add((row, col))

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  

                new_row = row + dr
                new_col = col + dc

                if dfs(new_row, new_col, word_index + 1, visited):
                    return True

        visited.remove((row, col)) 
        return False

    for start_row in range(rows):
        for start_col in range(cols):
            if dfs(start_row, start_col, 0, set()):
                return True

    return False
