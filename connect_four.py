def who_is_winner(pieces_position_list):

    board = [['' for _ in range(7)] for _ in range(6)]  

    for move in pieces_position_list:
        column, color = move.split('_')
        column_index = ord(column) - ord('A')

        for row in range(5, -1, -1):
            if board[row][column_index] == '':
                board[row][column_index] = color
                break

        if check_win(board, color):
            return color

    return "Draw"  


def check_win(board, color):

    for row in board:
        for i in range(4):
            if row[i:i+4] == [color] * 4:
                return True


    for col in range(7):
        for row in range(3):
            if all(board[row+i][col] == color for i in range(4)):
                return True

    for row in range(3):
        for col in range(4):
            if all(board[row+i][col+i] == color for i in range(4)):
                return True

    for row in range(3):
        for col in range(3, 7):
            if all(board[row+i][col-i] == color for i in range(4)):
                return True

    return False