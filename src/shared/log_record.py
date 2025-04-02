import time


class LogRecord:
    """Class that represents an individual log item to be written to log output"""
    level: int
    name: str
    message: object
    timestamp: int
    msecs: int
    asctime: object

    def __init__(self, name: str, level: int, message: object):
        """Initializes a new instance of the LogRecord class.
        :param name: The name of the logger.
        :param level: The level of the message.
        :param message: the message and / or content to log."""
        self.name = name
        self.level = level
        self.message = message
        self.ct = time.time()
        self.msecs = int((self.ct - int(self.ct)) * 1000)
        self.asctime = None