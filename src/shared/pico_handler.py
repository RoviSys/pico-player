from log_handler import (LogHandler)
from log_record import (LogRecord)
from log_level import (LogLevel)
from log_formatter import (LogFormatter)


class PicoHandler(LogHandler):
    """Class used to handle logging for a Raspberry Pi Pico"""

    def __init__(self, level: int = LogLevel.DEBUG, formatter: LogFormatter = LogFormatter()):
        """Initializes a new instance of the PicoHandler class.
        :param level: The minimum level to record logs for (only logs at or above this level are shown.)
        :param formatter: The LogFormatter instance used to format messages on the output log."""
        super().__init__(level, formatter)

    def emit(self, record: LogRecord):
        """Emit method that performs the actual logging.
        :param record: The LogRecord instance to log."""
        if (record.level >= self._level):
            print(self.format_output(record))
