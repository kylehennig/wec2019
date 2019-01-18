from game_logic import check_node

def random_guess(board, guess_board):
    pass

def guess_basin(board, guess_board):
    for i in range(len(board)):
        for j in range(len(board)):
                if guess_board[i][j].adjacent_basins == guess_board[i][j].adjacent_unvisited:
