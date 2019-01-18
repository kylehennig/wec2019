import tornado.websocket

from message import Message


class PlayerHandler(tornado.websocket.WebSocketHandler):
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

        if message.header == "CONNECT":
            pass
        else:
            message = Message("ERROR", "No request of that type exists.")
            self.write_message(message.json())

    def on_close(self):
        pass

    def check_origin(self, origin):
        return True
