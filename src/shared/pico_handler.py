from log_handler import (LogHandler)
from log_record import (LogRecord)
from log_level import (LogLevel)
from log_formatter import (LogFormatter)


class PicoHandler(LogHandler):
    def __init__(self, level: int = LogLevel.DEBUG, formatter: LogFormatter = LogFormatter()):
        super().__init__(level, formatter)

    def emit(self, record: LogRecord):
        print(self.format(record))
