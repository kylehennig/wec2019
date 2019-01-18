def check_node(x, y, board):
    board[x][y].set_visited()
    stop_checking = False
    # check if node is basin
    if board[x][y].basin:
        stop_checking = True
    # check left, right, up, down for adjacent basin
    if x != 0 and board[x-1][y].basin:
        board[x][y].increment_adjacent()
        stop_checking = True
    if x != len(board)-1 and board[x+1][y].basin:
        board[x][y].increment_adjacent()
        stop_checking = True
    if y != 0 and board[x-1][y-1].basin:
        board[x][y].increment_adjacent()
        stop_checking = True
    if y != len(board)-1 and board[x][y+1].basin:
        board[x][y].increment_adjacent()
        stop_checking = True
    # check left-up, left-down, right-down, right-up for basin
    if x != 0 and y != 0 and board[x-1][y-1].basin:
        board[x][y].increment_adjacent()
        stop_checking = True
    if x != 0 and y != len(board)-1 and board[x-1][y+1].basin:
        board[x][y].increment_adjacent()
        stop_checking = True
    if x != len(board)-1 and y != len(board)-1 and board[x+1][y+1].basin:
        board[x][y].increment_adjacent()
        stop_checking = True
    if x != len(board)-1 and y != 0 and board[x+1][y-1]:
        board[x][y].increment_adjacent()
        stop_checking = True
    # recursive base case
    if stop_checking:
        return
    # recursively check left, right, up, down nodes
    if x != 0 and not board[x-1][y].visited:
        check_node(x-1, y, board)
    if x != len(board)-1 and not board[x+1][y].visited:
        check_node(x+1, y, board)
    if y != 0 and not board[x][y-1].visited:
        check_node(x, y-1, board)
    if y != len(board)-1 and not board[x][y+1].visited:
        check_node(x, y+1, board)
