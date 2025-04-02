from log_record import (LogRecord)
import time

class LogFormatter:

    _default_fmt:str = "%(level)s:%(name)s:%(message)s"
    _default_datefmt:str = "%Y-%m-%d %H:%M:%S"
    _level_dict: dict = {
        0: "Debug",
        1: "Info",
        2: "Warn",
        3: "Error"
    }

    def __init__(self, fmt:str | None = None, datefmt:str | None = None):
        self.fmt = self._default_fmt if fmt is None else fmt
        self.datefmt = self._default_datefmt if datefmt is None else datefmt

    def uses_time(self):
        return "asctime" in self.fmt

    def format_time(self, datefmt: str, record: LogRecord):
        local_time = time.localtime(record.ct)
        return "{}/{}/{} {}:{}.{}".format(local_time[0], local_time[1], local_time[2], local_time[3], local_time[4], local_time[5])

    def format(self, record: LogRecord):
        if self.uses_time():
            record.asctime = self.format_time(self.datefmt, record)
        return self.fmt % {
            "name": record.name,
            "message": record.message,
            "msecs": record.msecs,
            "asctime": record.asctime,
            "level": self._level_dict[record.level],
        }