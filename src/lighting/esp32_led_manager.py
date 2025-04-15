from machine import (Pin)
import array
from neopixel import (NeoPixel)
from shared import Logger
from led_manager import (LEDManager)


class ESP32LEDManager(LEDManager):

    _pin: Pin
    _pixel: NeoPixel

    def __init__(self, gpio_num: int, led_names: list[str], logger: Logger):
        super().__init__(led_names, logger)
        self._pin = Pin(gpio_num, Pin.IN)
        self._pixel = NeoPixel(self._pin, self.led_count(), bpp=3, timing=1)

    def hide_all(self):
        """Turns off all of the LEds in the array."""
        for i in range(self.led_count()):
            self._pixel[i] = (0, 0, 0)
        self._pixel.write()
        self._sleep_ten()
    
    def set_brightness_for_all(self, brightness: float):
        """Sets the brightness level for all LEDs based on their current color.
        :param brightness: The brightness level to set (0 - 1)."""
        # NOTE: The I above represents a single bit for the value, H represents half-word, and B represents byte.
        for t in range(self.led_count()):
            current_color = self.load_led_by_index(t).current_color_rgb()
            self._pixel[t] = (int(current_color[0] * brightness), int(current_color[1] * brightness), int(current_color[2] * brightness)) 
        self._pixel.write()
        self._sleep_ten()