import sys

from web_socket_client import WebSocketClient

from bot import make_move
from server.message import Message

class BotClient(WebSocketClient):
    """Handles websockets for bots"""

    def __init__(self, url, bot):
        super().__init__(url)
        self.bot = bot

        message = Message("JOIN", "100")
        self.write_message(message.json())
        self.last_message = "JOIN"

    def on_message(self, message):
        """Handles messages from server"""
        message = Message.decode(message)

        if self.last_message == "JOIN":
            message = Message("BOARD")
            self.write_message(message.json())
            self.last_message = "BOARD"
        elif self.last_message == "BOARD":
            # TODO: parse board.
            make_move()
            self.last_message = "MOVE"
        elif self.last_message == "MOVE":
            message = Message("BOARD")
            self.write_message(message.json())
            self.last_message = "BOARD"
        elif message.header == "ERROR":
            print("ERROR")
            print(message.body)
            sys.exit(1)
        else:
            print("Unrecognized message header: {}".format(message.header))
