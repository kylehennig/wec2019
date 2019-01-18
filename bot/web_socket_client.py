from abc import ABC, abstractmethod

from tornado.websocket import websocket_connect


class WebSocketClient(ABC):
    default_timeout = 60

    def __init__(self, url, timeout=default_timeout):
        self.url = url
        self.timeout = timeout
        self.connection = None
        self.queued = []
        websocket_connect(self.url, callback=self.on_connection,
                          connect_timeout=timeout,
                          on_message_callback=self.on_message)

    def on_connection(self, future):
        self.connection = future.result()
        while len(self.queued) > 0:
            self.connection.write_message(self.queued.pop(0))

    @abstractmethod
    def on_message(self, message):
        pass

    def write_message(self, message):
        if self.connection is None:
            self.queued.append(message)
        else:
            self.connection.write_message(message)
