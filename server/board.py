import random
from math import sqrt

from server.node import Node


class Board:
    def __init__(self, size, seed):
        """
        Create the initial game board and randomly place catch basins.

        Args:
            size: The total amount of nodes in board.
            seed: The seed for pseudorandom numbers generation.
        """
        # create board of Node objects
        self.basin_count = int(sqrt(size))
        self.board = []
        for i in range(self.basin_count):
            self.board.append([])
            for _ in range(self.basin_count):
                self.board[i].append(Node())

        random.seed(seed)

        # place all catch basins randomly in nodes
        for i in range(self.basin_count):
            x = random.randint(0, self.basin_count - 1)
            y = random.randint(0, self.basin_count - 1)
            while self.board[x][y].basin:
                x = random.randint(0, self.basin_count - 1)
                y = random.randint(0, self.basin_count - 1)
            self.board[x][y].set_basin()

        # self.adjacent = []
        # for i in range(self.basin_count):
        #     self.board.append([])
        #     for j in range(self.basin_count):
        #         counter = 0
        #         self.board[i].append()

    def check_node(self, x, y):
        """
            Called when user clicks on a square and recurses upon adjacent nodes

            Args:
                x: x coordinate of node being checked
                y: y coordinate of node being checked
        """
        self.board[x][y].set_visited()
        stop_checking = False
        # check if node is basin
        if self.board[x][y].basin:
            stop_checking = True
        # check left, right, up, down for adjacent basin
        if x != 0 and self.board[x - 1][y].basin:
            self.board[x][y].increment_adjacent()
            stop_checking = True
        if x != len(self.board) - 1 and self.board[x + 1][y].basin:
            self.board[x][y].increment_adjacent()
            stop_checking = True
        if y != 0 and self.board[x - 1][y - 1].basin:
            self.board[x][y].increment_adjacent()
            stop_checking = True
        if y != len(self.board) - 1 and self.board[x][y + 1].basin:
            self.board[x][y].increment_adjacent()
            stop_checking = True
        # check left-up, left-down, right-down, right-up for basin
        if x != 0 and y != 0 and self.board[x - 1][y - 1].basin:
            self.board[x][y].increment_adjacent()
            stop_checking = True
        if x != 0 and y != len(self.board) - 1 and self.board[x - 1][y +
                                                                     1].basin:
            self.board[x][y].increment_adjacent()
            stop_checking = True
        if x != len(self.board) - 1 and y != len(self.board) - 1 and \
                self.board[x + 1][
                    y + 1].basin:
            self.board[x][y].increment_adjacent()
            stop_checking = True
        if x != len(self.board) - 1 and y != 0 and self.board[x + 1][y -
                                                                     1].basin:
            self.board[x][y].increment_adjacent()
            stop_checking = True
        # recursive base case
        if stop_checking:
            return
        # recursively check left, right, up, down nodes
        if x != 0 and not self.board[x - 1][y].visited:
            self.check_node(x - 1, y)
        if x != len(self.board) - 1 and not self.board[x + 1][y].visited:
            self.check_node(x + 1, y)
        if y != 0 and not self.board[x][y - 1].visited:
            self.check_node(x, y - 1)
        if y != len(self.board) - 1 and not self.board[x][y + 1].visited:
            self.check_node(x, y + 1)
        # recursively check left-up, left-down, right-down, right-up
        if x != 0 and y != 0 and not self.board[x - 1][y - 1].visited:
            self.check_node(x - 1, y - 1)
        if x != 0 and y != len(
                self.board) - 1 and not self.board[x - 1][y + 1].visited:
            self.check_node(x - 1, y + 1)
        if x != len(self.board) - 1 and y != len(self.board) - 1 and not \
                self.board[x + 1][
                    y + 1].visited:
            self.check_node(x + 1, y + 1)
        if x != len(self.board) - 1 and y != 0 and not self.board[x + 1][
                y - 1].visited:
            self.check_node(x + 1, y - 1)

    def serialize(self):
        serializable = []
        for i in range(self.basin_count):
            serializable.append([])
            for j in range(self.basin_count):
                serializable[i].append(self.board[i][j].serialize())
        return serializable
