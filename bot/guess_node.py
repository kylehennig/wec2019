class GuessNode:
    def __init__(self, x, y):
        coordinates = [x, y]
        adjacent_basins, adjacent_unvisited = check_adjacent(coordinates)

    def check_adjacent(self, coordinates):
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
        # check left-up,
        if x != 0 and y != 0 and not board[x-1][y].visited:
            unvisited_counter += 1
