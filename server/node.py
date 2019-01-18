from tornado.escape import json_encode


class Node:
    """Node objects that makes up board"""

    def __init__(self):
        self.visited = False
        self.basin = False
        self.adjacent = 0

    def set_basin(self):
        self.basin = True

    def set_visited(self):
        self.visited = True

    def increment_adjacent(self):
        self.adjacent += 1

    def json(self):
        dictionary = {
            "visited": self.visited,
            "basin": self.basin,
            "adjacent": self.adjacent
        }
        return json_encode(dictionary)
