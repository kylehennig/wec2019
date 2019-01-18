class GuessNode:
    def __init__(self, x, y, board):
        coordinates = [x, y]
        adjacent_basins, adjacent_unvisited = check_adjacent(coordinates, board)

    def check_adjacent(self, coordinates, board):
        unvisited_counter = 0
        # check left, up, right, down
        if x != 0 and not board[x-1][y].visited:
            unvisited_counter += 1
        if y != 0 and not board[x][y-1].visited:
            unvisited_counter += 1
        if x != len(board)-1 and not board[x+1][y].visited:
            unvisited_counter += 1
        if y != len(board)-1 and not board[x][y+1].visited:
            unvisited_counter += 1
        # check left-up, right-up, right-down, left-down
        if x != 0 and y != 0 and not board[x-1][y-1].visited:
            unvisited_counter += 1
        if x != len(board)-1 and y != 0 and not board[x+1][y-1].visited:
            unvisited_counter += 1
        if x != len(board)-1 and y != len(board)-1 and not board[x+1][y+1].visited:
            unvisited_counter += 1
        if x != 0 and y != len(board)-1 and not board[x-1][y+1].visited:
            unvisited_counter += 1
        return board[coordinates[0]][coordinates[1]].adjacent, unvisited_counter
