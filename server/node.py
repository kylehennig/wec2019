class Node:
    """Node objects that makes up board"""

    def __init__(self):
        self.visited = false
        self.basin = false
        self.adjacent = 0

    def set_basin(self):
        self.basin = true

    def set_visited(self):
        self.visited = true

    def increment_adjacent(self):
        self.adjacent += 1
