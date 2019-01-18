class GuessNode:
    def __init__(self, x, y, board):
        self.adjacent_basins, self.adjacent_unvisited = \
            self.check_adjacent(x, y, board)
        self.adjacent_known_basin = 0
        self.adjacent_known_not = 0
        self.unsure = True
        self.basin = False
        self.not_basin = False

    def check_adjacent(self, x, y, board):
        unvisited_counter = 0
        # check left, up, right, down
        if x != 0 and not board[x - 1][y].visited:
            unvisited_counter += 1
        if y != 0 and not board[x][y - 1].visited:
            unvisited_counter += 1
        if x != len(board) - 1 and not board[x + 1][y].visited:
            unvisited_counter += 1
        if y != len(board) - 1 and not board[x][y + 1].visited:
            unvisited_counter += 1
        # check left-up, right-up, right-down, left-down
        if x != 0 and y != 0 and not board[x - 1][y - 1].visited:
            unvisited_counter += 1
        if x != len(board) - 1 and y != 0 and not board[x + 1][y - 1].visited:
            unvisited_counter += 1
        if x != len(board) - 1 and y != len(board) - 1 and not board[x + 1][
            y + 1].visited:
            unvisited_counter += 1
        if x != 0 and y != len(board) - 1 and not board[x - 1][y + 1].visited:
            unvisited_counter += 1
        return board[x][y].adjacent, unvisited_counter

    def set_basin(self):
        self.unsure = False
        self.basin = True

    def set_not_basin(self):
        self.unsure = False
        self.not_basin = True
