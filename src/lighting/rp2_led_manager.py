import array
from shared import Logger
from led_manager import (LEDManager)
import rp2


class RP2LEDManager(LEDManager):
    """Manager type used to control LEDs in a series array configuration."""
    _state_machine: rp2.StateMachine

    def __init__(self, state_machine: rp2.StateMachine, led_names: list[str], logger: Logger):
        super().__init__(led_names, logger)
        """Initializes a new instance of the LEDManager class.
        :param state_machine: The Raspberry PI state machine instance for writing instructions to PIO assembly.
        :param led_names: The names the LEDs will be referred to.
        :param logger: The logger instance used to write log messages."""
        self._state_machine = state_machine

    def hide_all(self):
        """Turns off all of the LEds in the array."""
        dimmer_ar = array.array("I", [0 for _ in range(self.led_count())])
        for i in range(self.led_count()):
            dimmer_ar[i] = 0
        self._state_machine.put(dimmer_ar, 8)
        self._sleep_ten()

    def set_brightness_for_all(self, brightness: float):
        """Sets the brightness level for all LEDs based on their current color.
        :param brightness: The brightness level to set (0 - 1)."""
        dimmer_ar = list()
        # NOTE: The I above represents a single bit for the value, H represents half-word, and B represents byte.
        for t in range(self.led_count()):
            current_color = self.load_led_by_index(t).current_color()
            g = int(((current_color >> 8) & 0xFF) * brightness)
            r = int(((current_color >> 16) & 0xFF) * brightness)
            b = int((current_color & 0xFF) * brightness)
            dimmer_ar.append((g << 16) + (r << 8) + b)
        self._state_machine.put(array.array("I", dimmer_ar), 8)
        self._sleep_ten()
