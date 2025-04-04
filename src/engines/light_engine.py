from lighting import (LEDManager)
from shared import (Logger)
from drivers import (create_state_machine)
import rp2
import time


class LightEngine:
    """Engine used to encapsulate logic for controlling LEDs and sequencing."""

    _default_brightness: float
    _led_gpio: int
    _sm: rp2.StateMachine
    _light_logger: Logger
    _light_manager: LEDManager

    def __init__(self, led_gpio: int, default_brightness: float = 0.5):
        self._default_brightness = default_brightness
        self._led_gpio = led_gpio

        self._sm = create_state_machine(self._led_gpio)
        self._sm.restart()
        self._sm.active(1)
        self._light_logger = Logger('lights')
        self._light_manager = LEDManager(self._sm, ["1", "2"], self._light_logger)

    def light_all_for_duration(self, duration: int, color: tuple[int, int, int], brightness: float | None = None):
        self._light_logger.debug('Lighting all LEDs for ' + str(duration) + ' seconds.')
        self._light_manager.set_color_for_all(color)
        self._light_manager.set_brightness_for_all(self._default_brightness if brightness is None else brightness)
        time.sleep(duration)
        self._light_manager.hide_all()
        self._light_logger.debug('done')

    def rainbow_cycle(self, wait: float):
        self._light_logger.debug("Starting rainbow cycle.")
        for j in range(255):
            for i in range(self._light_manager.led_count()):
                rc_index = (i * 256 // self._light_manager.led_count()) + j
                self._light_manager.set_color(i, self._wheel(rc_index & 255))
            self._light_manager.set_brightness_for_all(self._default_brightness)
            time.sleep(wait)
        self._light_logger.debug("Cycle finished")

    def all_off(self):
        self._light_manager.hide_all()

    def _wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)
