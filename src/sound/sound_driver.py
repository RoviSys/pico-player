from shared import (Logger, constants)


class SoundDriver:
    """Base class for sound drivers"""

    _logger: Logger
    _adjusted_volume: float

    def __init__(self, logger: Logger, adjusted_volume: float | None = None):
        """Initializes a new instance of the SoundDriver class.
        :param logger: The logger instance used to write log messages.
        :param adjusted_volume: The default volume (percentage from 0 - 1) multiplier to use for sound."""
        self._logger = logger
        # Some one-liner checks to make sure that adjusted volume falls between 0 and 1
        self._adjusted_volume = .25 if adjusted_volume is None else 1 if adjusted_volume > 1 else 0 if adjusted_volume < 0 else adjusted_volume

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

    def _calculate_volume(self, tone_volume: int) -> int:
        """Returns the calculated frequency based on the adjusted volume level and the given tone_volume.
        :param tone_volume: The volume of the specific tone."""
        max_volume = int(constants.MAX_FREQUENCY * self._adjusted_volume)
        tone_ratio = tone_volume / max_volume
        computed_volume = int(tone_ratio * tone_volume * 100)

        if computed_volume > max_volume:
            return max_volume

        return computed_volume
