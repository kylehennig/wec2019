from node import Node
import random

def generate(size):
    """
    Create the Initial Game Board and Catch Basins

    Args:
        size: total amount of nodes in board

    Returns:
        board: an array of node objects
    """

    board = [[]*sqrt(size)]*sqrt(size)
    for i in range(sqrt(size)):
        for j in range(sqrt(size)):
            board[i][j] = Node()

    for i in range(sqrt(size)):
        x = random.randint(0, sqrt(size)-1)
        y = random.randint(0, sqrt(size)-1)
        while board[x][y].basin:
            x = random.randint(0, sqrt(size)-1)
            y = random.randint(0, sqrt(size)-1)
        board[x][y].set_basin()

    return board
