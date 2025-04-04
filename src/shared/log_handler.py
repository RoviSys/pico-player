from log_level import (LogLevel)
from log_record import (LogRecord)
from log_formatter import (LogFormatter)


class LogHandler:
    _formatter: LogFormatter
    _level: int

    def __init__(self, level=LogLevel.DEBUG, formatter=LogFormatter()):
        self._level = level
        self._formatter = formatter

    def close(self):
        pass

    def set_level(self, level: int):
        self._level = level

    def format_output(self, record: LogRecord) -> str:
        return self._formatter.format_message(record)

    def emit(self, record: LogRecord):
        """Emits the error
        :param record: The LogRecord instance to log"""
        pass
