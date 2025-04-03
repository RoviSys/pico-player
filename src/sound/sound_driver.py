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

    def tone(self, tone_data: tuple[str, float, int]):
        """Plays a tone on a buzzer.
        :param tone_data: The tone tuple to play (ex: ("A2", 2, 3000)) where 'A2' is the tone to play, 2 is the duration, and 3000 is the volume (from 0 - 65535)"""  # noqa: E501
        pass

    def quiet(self, tone_data: tuple[str, float, int] | None = None):
        """Quiets the buzzer.
        :param tone_data: The tone tuple to play (ex: ("P", 2, 3000)).  The argument is optional.  When provided, the ONLY valid 1st tuple argument is "P" for Pause, and the volume is ignored. Position 2 is the duration."""  # noqa: E501
        pass
