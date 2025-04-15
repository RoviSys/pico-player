import array
from shared import Logger
from led_array import (LEDArray)
from led import (LED)
import rp2
import time


class LEDManager:
    """Manager type used to control LEDs in a series array configuration."""
    _leds: LEDArray
    _led_names: list[str]
    _logger: Logger

    def __init__(self, led_names: list[str], logger: Logger):
        """Initializes a new instance of the LEDManager class.
        :param led_names: The names the LEDs will be referred to.
        :param logger: The logger instance used to write log messages."""
        self._led_names = led_names
        self._initialize_leds()
        self._logger = logger

    def _initialize_leds(self):
        """Performs initial setup of the LED array based on the inputs"""
        self._leds = LEDArray(len(self._led_names), self._led_names)

    def hide_all(self):
        """Turns off all of the LEds in the array."""
        pass

    def load_led_by_name(self, name: str) -> LED:
        """Attempts to return an LED instance from the array that matches the given name.
        :param name: The name of the LED to find."""
        for i in range(self.led_count()):
            current_led = self._leds.leds[i]
            if current_led.name == name:
                return current_led
        return LED("Empty")

    def find_led_index(self, name: str) -> int:
        """Attempts to find the index of an LED based on it's name.  Useful in situations where an indexer is needed for control.
        :param name: The name of the LED to find."""
        for i in range(self.led_count()):
            current_led = self._leds.leds[i]
            if current_led.name == name:
                return i
        return 0

    def load_led_by_index(self, index: int) -> LED:
        """Attempts to return an LED instance matching the given index.  Useful when the name is not known (like when iterating)."""
        return self._leds.leds[index]

    def set_color(self, i: int, color: tuple[int, int, int]):
        """Sets the color for an individual LED at the given index.  This method does not illuminate the LED, it just changes it's color state.
        :param i: The index of the LED to set.
        :param color: The color to set the LED to."""
        self._logger.debug((i, color))
        self._leds.leds[i].set_color(color[1], color[0], color[2])

    def set_brightness_for_all(self, brightness: float):
        """Sets the brightness level for all LEDs based on their current color.
        :param brightness: The brightness level to set (0 - 1)."""
        pass

    def set_color_for_all(self, color: tuple[int, int, int]):
        """Convenience method for setting all of the LEDs to a specific color."""
        for i in range(self.led_count()):
            self.set_color(i, color)

    def _sleep_ten(self):
        """Sleeps for 10 milliseconds on the current thread."""
        time.sleep_ms(10)

    def led_count(self) -> int:
        """Returns the number of LEDs in the array.  Mostly a wrapper."""
        return self._leds.length()
