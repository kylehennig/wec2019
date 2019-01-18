import random
from math import sqrt
from tornado.escape import json_encode

from node import Node


class Board():
    def __init__(self, size, seed):
        """
        Create the initial game board and randomly place catch basins.

        Args:
            size: The total amount of nodes in board.
            seed: The seed for pseudorandom numbers generation.
        """
        self.basin_count = int(sqrt(size))
        self.board = []
        for i in range(self.basin_count):
            self.board.append([])
            for _ in range(self.basin_count):
                self.board[i].append(Node())

        random.seed(seed)

        for i in range(self.basin_count):
            x = random.randint(0, self.basin_count - 1)
            y = random.randint(0, self.basin_count - 1)
            while self.board[x][y].basin:
                x = random.randint(0, self.basin_count - 1)
                y = random.randint(0, self.basin_count - 1)
                self.board[x][y].set_basin()

    def json(self):
        serializable = []
        for i in range(self.basin_count):
            serializable.append([])
            for j in range(self.basin_count):
                serializable[i].append(self.board[i][j].json())
        return json_encode(serializable)
