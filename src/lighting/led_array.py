from led import (LED)


class LEDArray:
    """Class used to manage a read-only array of LEDs that have "words" associated with them as well as some convenience functions."""
    _array_size: int
    _leds: list[LED]

    def __init__(self, array_size: int, names: list[str]):
        """Initializes a new LEDArray instance.
        :param array_size: The number of LEDs in the array.
        :param names: The set of names used to "address" the LEDs in the array."""
        self._array_size = array_size
        self._leds = list()

        for i in range(self._array_size):
            new_led = LED(names[i])
            self._leds.append(new_led)

    @property
    def leds(self) -> list[LED]:
        """Property used to load the set of LEDs in the array."""
        return self._leds

    def length(self) -> int:
        """Returns the number of LEDs in the array."""
        return len(self._leds)
