from bot.guess_node import GuessNode

class GuessBoard:
    """
        Create the Bot's Guess Board. This is the bot's 'memory'
    """
    def __init__(self, board):
        self.basin_count = len(board)
        self.guess_board = []
        for i in range(self.basin_count):
            self.guess_board.append([])
            for _ in range(self.basin_count):
                self.guess_board[i].append(GuessNode())

    def count_known_basin(self):
        for i in range(self.basin_count):
            for j in range(self.basin_count):
                count = 0
                if i != 0 and self.guess_board[i-1][j].basin:
                    count += 1
                if j != 0 and self.guess_board[i][j-1].basin:
                    count += 1
                if i != self.basin_count-1 and self.guess_board[i+1][j].basin:
                    count += 1
                if j != self.basin_count-1 and self.guess_board[i][j+1].basin:
                    count += 1
                if i != 0 and j != 0 and self.guess_board[i-1][j-1].basin:
                    count += 1
                if i != 0 and j != self.basin_count-1 and self.guess_board[i-1][j+1].basin:
                    count += 1
                if i != self.basin_count-1 and j != self.basin_count-1 and self.guess_board[i+1][j+1].basin:
                    count += 1
                if i != self.basin_count-1 and j != 0 and self.guess_board[i+1][j-1].basin:
                    count += 1
                self.guess_board[i][j].adjacent_known_basin = count

    def check_for_basin(self, board):
        for i in range(self.basin_count):
            for j in range(self.basin_count):
                if self.guess_board[i][j].adjacent_basins == self.guess_board[i][j].adjacent_unvisited:
                    if i != 0 and not board[i-1][j].visited:
                        self.guess_board[i-1][j].set_basin()
                    if j != 0 and not board[i][j-1].visited:
                        self.guess_board[i][j-1].set_basin()
                    if i != self.basin_count-1 and not board[i+1][j].visited:
                        self.guess_board[i+1][j].set_basin()
                    if j != self.basin_count-1 and not board[i][j+1].visited:
                        self.guess_board[i][j+1].set_basin()
                    if i != 0 and j != 0 and not board[i-1][j-1].visited:
                        self.guess_board[i-1][j-1].set_basin()
                    if i != 0 and j != self.basin_count-1 and not board[i-1][j+1].visited:
                        self.guess_board[i-1][j+1].set_basin()
                    if i != self.basin_count-1 and j != self.basin_count-1 and not board[i+1][j+1].visited:
                        self.guess_board[i+1][j+1].set_basin()
                    if i != self.basin_count-1 and j != 0 and not board[i+1][j-1].visited:
                        self.guess_board[i+1][j-1].set_basin()

        def check_for_not_basin(self, board):
            for i in range(self.basin_count):
                for j in range(self.basin_count):
                    if self.guess_board[i][j].adjacent_known_basin == self.board[i][j].adjacent:
                        if i != 0 and not board[i-1][j].visited:
                            self.guess_board[i-1][j].set_not_basin()
                        if j != 0 and not board[i][j-1].visited:
                            self.guess_board[i][j-1].set_not_basin()
                        if i != self.basin_count-1 and not board[i+1][j].visited:
                            self.guess_board[i+1][j].set_not_basin()
                        if j != self.basin_count-1 and not board[i][j+1].visited:
                            self.guess_board[i][j+1].set_not_basin()
                        if i != 0 and j != 0 and not board[i-1][j-1].visited:
                            self.guess_board[i-1][j-1].set_not_basin()
                        if i != 0 and j != self.basin_count-1 and not board[i-1][j+1].visited:
                            self.guess_board[i-1][j+1].set_not_basin()
                        if i != self.basin_count-1 and j != self.basin_count-1 and not board[i+1][j+1].visited:
                            self.guess_board[i+1][j+1].set_not_basin()
                        if i != self.basin_count-1 and j != 0 and not board[i+1][j-1].visited:
                            self.guess_board[i+1][j-1].set_not_basin()
