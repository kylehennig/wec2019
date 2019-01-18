def check_node(x, y, board):
    if board[x][y].basin:
        pass
    if x != 0 and not board[x-1][y].visited:
        pass
    if x != len(board)-1 and not board[x+1][y].visited:
        pass
    if y != 0 and not board[x][y-1].visited:
        pass
    if y != len(board)-1 and not board[x][y+1].visited:
        pass
