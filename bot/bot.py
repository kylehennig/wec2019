import random

from bot.guess_board import GuessBoard


def make_move(board):
    """
        Function used to play game with bot

        Args:
            board: Game board object
    """
    bot_board = GuessBoard()

    bot_board.check_for_basin(board)
    bot_board.count_known_basin()
    bot_board.check_for_not_basin()
    x = -1
    y = -1
    # Bot selects first unvisited node that is known to not be a basin
    for i in range(bot_board.basin_count):
        for j in range(bot_board.basin_count):
            if bot_board.guess_board[i][j].not_basin and not board[i][j].visited:
                x = i
                y = j
    if x != -1 and y != -1:
        pass
    # If there are no nodes that are known to not be basin randomly select node
    else:
        x = random.randint(0, bot_board.basin_count - 1)
        y = random.randint(0, bot_board.basin_count - 1)
        while board[i][j].visited:
            x = random.randint(0, bot_board.basin_count - 1)
            y = random.randint(0, bot_board.basin_count - 1)

    return x, y
