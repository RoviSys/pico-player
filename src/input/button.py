from machine import (Pin)
from shared import (Logger)
import time


class Button:
    """Class used to represent a button capable of controlling things."""

    _pin: Pin
    _logger: Logger
    _interrupt: bool
    _debounce_timer: int

    def __init__(self, logger: Logger, gpio_num: int, interrupt: bool):
        """Initializes a new instance of the button class.
        :param logger: The logger instance used to write log messages.
        :param gpio_num: The gpio number to use for the button.
        :param interrupt: Used to stop the listen function.  Typically a variable handled elsewhere to interrupt the listener."""
        self._pin = Pin(gpio_num, Pin.IN, Pin.PULL_DOWN)
        self._logger = logger
        self._interrupt = interrupt
        self._debounce_timer = time.ticks_ms()

    def listen(self, handler):
        """Use this method to provide a callback that is executed when the button is pressed.
        :param handler: A function to execute when the button is pressed."""
        while self._interrupt is False:
            if self._pin.value() is True:
                current_time = time.ticks_ms()

                time_passed = time.ticks_diff(current_time, self._debounce_timer)

                if time_passed > 500:
                    self._logger.debug("Button press")
                    handler()
                else:
                    self._logger.debug("Debounce Detection")

        self._logger.debug("Hanging up the phone")
