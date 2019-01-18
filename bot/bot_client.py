import sys

import tornado.ioloop

from bot.bot import make_move
from bot.web_socket_client import WebSocketClient
from server.board import Board
from server.message import Message


class BotClient(WebSocketClient):
    """Handles websockets for bots"""

    def __init__(self, url, size):
        super().__init__(url)
        message = Message("JOIN", {"size": size})
        self.write_message(message.json())
        self.last_message = "JOIN"

    def on_message(self, message):
        """Handles messages from server"""
        message = Message.decode(message)

        if self.last_message == "JOIN":
            message = Message("BOARD", "")
            self.write_message(message.json())
            self.last_message = "BOARD"
        elif self.last_message == "BOARD":
            board = message.body["board"]
            board = Board.from_json(board)
            x, y = make_move(board)
            message = Message("MOVE", {"x": x, "y": y})
            self.write_message(message.json())
            self.last_message = "MOVE"
        elif self.last_message == "MOVE":
            message = Message("BOARD", "")
            self.write_message(message.json())
            self.last_message = "BOARD"
        elif message.header == "ERROR":
            print("ERROR")
            print(message.body)
            sys.exit(1)
        else:
            print("Unrecognized message header: {}".format(message.header))


def main():
    url = "ws://localhost:8888/player"
    if len(sys.argv) == 1:
        BotClient(url, 100)
    elif len(sys.argv) == 2:
        size = int(sys.argv[2])
        BotClient(url, size)
    else:
        print("Usage: python3 run_bot.py <size>")

    tornado.ioloop.IOLoop.current().start()
