import random
from math import sqrt

from node import Node


def generate(size, seed):
    """
    Create the Initial Game Board and Catch Basins

    Args:
        size: total amount of nodes in board
        seed: seed for psuedorandom numbers

    Returns:
        board: an array of node objects
    """
    basin_count = int(sqrt(size))
    board = [[] * basin_count] * basin_count
    for i in range(basin_count):
        for j in range(basin_count):
            board[i][j] = Node()

    random.seed(seed)

    for i in range(basin_count):
        x = random.randint(0, basin_count - 1)
        y = random.randint(0, basin_count - 1)
        while board[x][y].basin:
            x = random.randint(0, basin_count - 1)
            y = random.randint(0, basin_count - 1)
        board[x][y].set_basin()

    return board
