import time

import tornado.ioloop
import tornado.web
import tornado.websocket

from server.board import Board
from server.message import Message


class PlayerHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.board = None

    def open(self):
        pass

    def on_message(self, message):
        try:
            message = Message.decode(message)
        except Exception as e:
            # Replies with an error.
            message = Message("ERROR", str(e))
            self.write_message(message.json())
            # Logs the error to a file.
            with open("server.log", "a") as file:
                file.write("ERROR: " + str(e))
            return

        if message.header == "JOIN":
            # Makes sure a user has not already joined.
            if self.board is not None:
                message = Message("ERROR", "A game is already in progress.")
                self.write_message(message.json())
                return

            # Checks mandatory params.
            try:
                size = message.body["size"]
            except KeyError:
                message = Message("ERROR", "Bad join request.")
                self.write_message(message.json())
                return

            # Checks optional params.
            if "seed" in message.body:
                seed = message.body["seed"]
            else:
                seed = time.time()

            # Generates the game board.
            self.board = Board(size, seed)

            # Replies when done.
            message = Message("DONE", {"success": True})
            self.write_message(message.json())
        elif message.header == "BOARD":
            # Ensures a user has already joined.
            if self.board is None:
                message = Message("ERROR", "Please join a game first.")
                self.write_message(message.json())
                return

            # Replies with the current state of the board.
            message = Message(
                "DONE", {"success": True, "board": self.board.serialize()}
            )
            self.write_message(message.json())
        elif message.header == "MOVE":
            # Ensures a user has already joined.
            if self.board is None:
                message = Message("ERROR", "Please join a game first.")
                self.write_message(message.json())
                return

            # Checks mandatory params.
            try:
                x = message.body["x"]
                y = message.body["y"]
            except KeyError:
                message = Message("ERROR", "Bad join request.")
                self.write_message(message.json())
                return

            # Checks that x and y are in bounds.
            if x >= self.board.basin_count or y >= self.board.basin_count:
                message = Message(
                    "ERROR", "Selected coordinate is out of bounds."
                )
                self.write_message(message.json())
                return

            # Updates the game board.
            self.board.check_node(x, y)

            # Replies when done.
            message = Message("DONE", {"success": True})
            self.write_message(message.json())
        else:
            message = Message("ERROR", "No request of that type exists.")
            self.write_message(message.json())

    def on_close(self):
        pass

    def check_origin(self, origin):
        return True


def main():
    # Starts the web server.
    app = tornado.web.Application([
        (r"/player", PlayerHandler)
    ])
    port = 8888
    print("Starting server on port {}.".format(port))
    app.listen(port)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("Server stopped.")


if __name__ == "__main__":
    main()
