from node import node
import random

def generate(size):
    board = [[]*sqrt(size)]*sqrt(size)
    for i in range(sqrt(size)):
        for j in range(sqrt(size)):
            board[i][j] = node()

    for i in range(sqrt(size)):
        x = random.randint(0, sqrt(size)+1)
        y = random.randint(0, sqrt(size)+1)
        while board[x][y].basin:
            x = random.randint(0, sqrt(size)+1)
            y = random.randint(0, sqrt(size)+1)
        board[x][y].set_basin()
