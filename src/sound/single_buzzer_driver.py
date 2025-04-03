from machine import (Pin, PWM)
from sound_driver import (SoundDriver)
from tones import (tones)
from shared import (constants, Logger)
import time


class SingleBuzzerDriver(SoundDriver):
    """Type used to drive a single buzzer for sound output."""

    _buzzer: PWM

    def __init__(self, logger: Logger, gpio_num: int):
        """Initializes a new instance of the SingleBuzzerDriver class.
        :param logger: The Logger instance used to write log messages.
        :param gpio_number: The gpio number on which the buzzer driver is configured."""
        super().__init__(logger)
        self._buzzer = PWM(Pin(gpio_num), duty_u16=int(constants.MAX_INT//2))
        self._buzzer.init()

    def _get_duration(self, tone_data: tuple[str, float, int]) -> float:
        return 0.6 * tone_data[1]

    def tone(self, tone_data: tuple[str, float, int]):
        duration = self._get_duration(tone_data)
        self._logger.debug("Playing " + tone_data[0] + " for " + str(duration) + " seconds.")
        self._logger.debug(tones[tone_data[0]])
        self._buzzer.freq(tones[tone_data[0]])
        self._buzzer.duty_u16(tone_data[2])
        time.sleep(duration)

    def quiet(self, tone_data: tuple[str, float, int] | None = None):
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
