from log_record import (LogRecord)
import time


class LogFormatter:
    """Class used to handle logic for formatting log messages before being written."""

    _default_fmt: str = "%(level)s:%(name)s:%(message)s"
    _default_datefmt: str = "%Y-%m-%d %H:%M:%S"
    _level_dict: dict = {
        0: "Debug",
        1: "Info",
        2: "Warn",
        3: "Error"
    }

    def __init__(self, fmt: str | None = None):
        """Initializes a new instance of the LogFormatter class.
        :param fmt: The format of the log message (defaults to a standard format if none is provided)."""
        self.fmt = self._default_fmt if fmt is None else fmt

    def uses_time(self) -> bool:
        """Determines whether or not the formatter instance can format time data as part of the log format."""
        return "asctime" in self.fmt

    def format_time(self, record: LogRecord) -> str:
        """Formats the date / time portion of the record into a readable format.
        :param record: The LogRecord instance with time information to format."""
        local_time = time.localtime(record.ct)
        return "{}/{}/{} {}:{}.{}".format(local_time[0], local_time[1], local_time[2], local_time[3], local_time[4], local_time[5])

    def format_message(self, record: LogRecord) -> str:
        """Formats the given record in a standard way for logging.
        :param record: The LogRecord instance being formatted."""
        if self.uses_time():
            record.asctime = self.format_time(record)
        return self.fmt % {
            "name": record.name,
            "message": record.message,
            "msecs": record.msecs,
            "asctime": record.asctime,
            "level": self._level_dict[record.level],
        }
