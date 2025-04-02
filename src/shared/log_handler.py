from log_level import (LogLevel)
from log_record import (LogRecord)
from log_formatter import (LogFormatter)


class LogHandler:
    _formatter: LogFormatter

    def __init__(self, level=LogLevel.DEBUG, formatter=LogFormatter()):
        self.level = level
        self.formatter = formatter

    def close(self):
        pass

    def set_level(self, level: LogLevel):
        self.level = level

    def set_formatter(self, formatter: LogFormatter):
        self.formatter = formatter

    def format(self, record: LogRecord) -> str:
        return self.formatter.format(record)
    
    def emit(self, record: LogRecord):
        """Emits the error
        :param record: The LogRecord instance to log"""
        pass