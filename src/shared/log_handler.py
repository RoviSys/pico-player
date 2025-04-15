from log_level import (LogLevel)
from log_record import (LogRecord)
from log_formatter import (LogFormatter)


class LogHandler:
    """Abstract class used for inherited classes that handle log specifics for a platform / output."""
    _formatter: LogFormatter
    _level: int

    def __init__(self, level=LogLevel.DEBUG, formatter=LogFormatter()):
        """Initializes a new instance of the LogHandler class.
        :param level: The minimum level to record logs for (only logs at or above this level are shown.)
        :param formatter: The LogFormatter instance used to format messages on the output log."""
        self._level = level
        self._formatter = formatter

    def close(self):
        """Performs any cleanup / close operations on the log handler (if any)."""
        pass

    def set_level(self, level: int):
        """Allows the log level to be changed after the handler has been created.
        :param level: The new log level to configure."""
        self._level = level

    def format_output(self, record: LogRecord) -> str:
        """Performs output formatting of the record prior to logging.
        :param record: The LogRecord instance being logged."""
        return self._formatter.format_message(record)

    def emit(self, record: LogRecord):
        """Emits the error.  Designed to be overridden with specific logic in inherited classes.
        :param record: The LogRecord instance to log"""
        pass
