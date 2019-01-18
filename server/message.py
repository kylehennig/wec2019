from tornado.escape import json_encode, json_decode


class Message:
    """Defines a message for communication between the server and client."""

    def __init__(self, header, body):
        self.header = header
        self.body = body

    def json(self):
        """Converts the message to JSON.

        Returns:
            The JSON representation of the message.
        """
        return json_encode({"header": self.header, "body": self.body})

    @staticmethod
    def decode(message):
        """Decodes a message from JSON.

        Args:
            message: The JSON string to decode.

        Returns:
            A message instance created from the provided JSON.
        """
        message = json_decode(message)
        if "body" in message:
            return Message(message["header"], message["body"])
        else:
            return Message(message["header"], None)
