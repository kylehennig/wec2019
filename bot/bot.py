from guess_node import GuessNode
from guess_basin import random_guess

def bot(board):
    basin_count = len(board)
    guess_board = []
    for i in range(basin_count):
        guess_board.append([])
        for _ in range(basin_count):
            guess_board[i].append(GuessNode())
    game = random_guess()
    while game:
        
