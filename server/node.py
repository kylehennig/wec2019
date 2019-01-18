class node:
    def __init__(self):
        self.visited = false
        self.basin = false

    def set_basin(self):
        self.basin = true

    def set_visited(self):
        self.visited = true
