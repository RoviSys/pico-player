from machine import (Pin, PWM)
from sound_driver import (SoundDriver)
from tones import (tones)
from shared import (constants, Logger)
import time


class SingleBuzzerDriver(SoundDriver):
    """Type used to drive a single buzzer for sound output."""

    _buzzer: PWM

    def __init__(self, logger: Logger, gpio_num: int, adjusted_volume: float | None = None):
        """Initializes a new instance of the SingleBuzzerDriver class.
        :param logger: The Logger instance used to write log messages.
        :param gpio_number: The gpio number on which the buzzer driver is configured.
        :param adjusted_volume: The volume adjustment for tones."""
        super().__init__(logger, adjusted_volume)
        self._buzzer = PWM(Pin(gpio_num), duty_u16=int(constants.MAX_INT//2))
        self._buzzer.init()

    def _get_duration(self, tone_data: tuple[str, float, int]) -> float:
        """Calculates the duration a tone should be played for based on the given tone data.
        :param tone_data: The tuple with tone information (ex: ("A2", 2, 3000) where "A2" is the tone, 2 is the duration, and 3000 is the volume (0 - 65535))."""  # noqa: E501
        return 0.6 * tone_data[1]

    def tone(self, tone_data: tuple[str, float, int]):
        """Plays a tone on a buzzer.
        :param tone_data: The tone tuple to play (ex: ("A2", 2, 3000)) where 'A2' is the tone to play, 2 is the duration, and 3000 is the volume (from 0 - 65535)"""  # noqa: E501
        if tone_data is None:
            self._logger.error("No tone data provided.")
            return

        if tone_data[0] in tones:
            duration = self._get_duration(tone_data)
            self._logger.debug("Playing " + tone_data[0] + " for " + str(duration) + " seconds with a duty cycle of " + str(tones[tone_data[0]]) + ".")
            self._buzzer.freq(tones[tone_data[0]])
            self._buzzer.duty_u16(self._calculate_volume(tone_data[2]))
            time.sleep(duration)
        else:
            self._logger.warn("An unrecognized tone was given: " + str(tone_data[0]) + ".")

    def quiet(self, tone_data: tuple[str, float, int] | None = None):
        """Quiets the buzzer.
        :param tone_data: The tone tuple to play (ex: ("P", 2, 3000)).  The argument is optional.  When provided, the ONLY valid 1st tuple argument is "P" for Pause, and the volume is ignored. Position 2 is the duration."""  # noqa: E501
        if tone_data is None:
            self._buzzer.duty_u16(0)
        else:
            duration = self._get_duration(tone_data)
            self._buzzer.duty_u16(0)
            time.sleep(duration)

    def off(self):
        """Turns the buzzer off."""
        self.quiet()
        self._buzzer.deinit()
