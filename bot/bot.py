from guess_node import GuessNode
from guess_board import GuessBoard
from guess_basin import random_guess
import random

def bot(board):

    bot_board = GuessBoard()
    while True:
        bot_board.check_for_basin(board)
        bot_board.count_known_basin()
        bot_board.check_for_not_basin()
        check_coords = [-1, -1]
        for i in range(bot_board.basin_count):
            for j in range(bot_board.basin_count):
                if bot_board.guess_board[i][j].not_basin and not board[i][j].visited:
                    check_coords = [i, j]
        if check_coords[0] != -1:
            pass
        else:
            x = random.randint(0, bot_board.basin_count - 1)
            y = random.randint(0, bot_board.basin_count - 1)
            while board[i][j].visited:
                x = random.randint(0, bot_board.basin_count - 1)
                y = random.randint(0, bot_board.basin_count - 1)
            check_coords = [x, y]
        # TODO: make bot take turn
