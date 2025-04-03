from shared import (Logger)


class SoundDriver:
    """Base class for sound drivers"""

    _logger: Logger

    def __init__(self, logger: Logger):
        """Initializes a new instance of the SoundDriver class.
        :param logger: The logger instance used to write log messages."""
        self._logger = logger

    def off(self):
        """Turns the sound off."""
        pass

    def tone(self, tone: tuple[str, float, int]):
        pass

    def quiet(self, tone_data: tuple[str, float, int] | None = None):
        pass
