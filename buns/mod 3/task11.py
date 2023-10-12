def check(board):
    size = len(board)
    for row in board:
        if row.count('X') == size:
            return 'X'
        elif row.count('O') == size:
            return 'O'
    for c in range(size):
        col = [board[row][c] for row in range(size)]
        if col.count('X') == size:
            return 'X'
        elif col.count('O') == size:
            return 'O'
    d1 = [board[i][i] for i in range(size)]
    d2 = [board[i][size - i - 1] for i in range(size)]
    if d1.count('X') == size or d2.count('X') == size:
        return 'X'
    elif d1.count('O') == size or d2.count('O') == size:
        return 'O'


board = [list(input())]
for i in range(len(board[0])-1):
    board.append(list(input()))
print(check(board))