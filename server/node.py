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

    def serialize(self):
        serializable = {
            "visited": self.visited,
            "basin": self.basin,
            "adjacent": self.adjacent
        }
        return serializable

    @staticmethod
    def from_json(json):
        node = Node()
        node.visited = json["visited"]
        node.basin = json["basin"]
        node.adjacent = json["adjacent"]
        return node
