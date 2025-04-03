from .log_level import (LogLevel)
from .log_formatter import (LogFormatter)
from .pico_handler import (PicoHandler)
from .log_handler import (LogHandler)
from .log_record import (LogRecord)


class Logger:
    """A wrapper around the default logger with a bit more control over log granularity and logic"""

    __default_fmt: str = "[%(asctime)s.%(msecs)03d - %(level)s:%(name)s] %(message)s"
    _formatter: LogFormatter
    _handler: LogHandler

    def __init__(self, name, default_level=LogLevel.DEBUG):
        """Initializes a new instance of the Logger class.
        :param name: The name of the logger to create.
        :param default_level: The default LogLevel to allow writes for.  Only messages at or higher than this will be logged."""
        self.__name = name
        self._formatter = LogFormatter(self.__default_fmt)
        self._handler = PicoHandler(default_level, self._formatter)
        # In the form: [(Project Name)] - message

    def set_level(self, level):
        """Sets the default log level for this logger instance."""
        self._handler.set_level(level)

    def info(self, message):
        """Writes an informational-level message.
        :param message: The message to write."""
        self._write_log(LogLevel.INFO, message)

    def debug(self, message):
        """Writes a debug-level message.
        :param message: The message to write."""
        self._write_log(LogLevel.DEBUG, message)

    def warn(self, message):
        """Writes a warning-level message.
        :param message: The message to write."""
        self._write_log(LogLevel.WARN, message)

    def error(self, message):
        """Writes an error-level message.
        :param message: The message to write."""
        self._write_log(LogLevel.ERROR, message)

    def _write_log(self, level: int, message):
        """Internal method that determines whether the message should be logged based on the level.
        :param level: The level of the log, which is compared against configuration of the logger.
        :param message: The message to write."""
        record = LogRecord(self.__name, level, message)
        self._handler.emit(record)
