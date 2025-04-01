from machine import (Pin, ADC)
from shared import (constants)
import sys


class PiPico:
    """Type used to encapsulate system calls for Raspberry PI Pico micro controllers."""

    # State / configuration
    _has_onboard_led: bool
    _is_pico_w: bool
    _conversion_factor: float = 3.3 / constants.MAX_ADC

    # Pins and common hardware
    _led_pin: Pin | None
    _temperature_pin: ADC | None
    _vsys_pin: ADC | None

    def __init__(self, is_pico_w: bool = False, has_on_board_led: bool = True):
        """Initializes a new instance of the PiPico class for controlling a Raspberry PI instance.
        :param is_pico_w: True for Pico W support (default is False)
        :param has_on_board_led: False to change how the on-board LED is accessed (default is True)"""
        self._is_pico_w = is_pico_w
        self._has_onboard_led = has_on_board_led
        self._led_pin = None
        self._temperature_pin = None
        self._vsys_pin = None

    def __init_led_pin(self):
        """A re-entrant method that performs one-time initialization of the Onboard LED PIN.  Used internally when necessary."""
        if (self._led_pin is None):
            if (self._is_pico_w):
                self._led_pin = Pin("LED", Pin.OUT)
            else:
                self._led_pin = Pin(constants.PICO_ONBOARD_LED_PIN, Pin.OUT)

    def __init_temp_pin(self):
        """A re-entrant method that performs one-time initialization of the temperature ADC pin.  Used internally when necessary."""
        if (self._temperature_pin is None):
            self._temperature_pin = ADC(4)

    def __init_vsys_pin(self):
        """A re-entrant method that performs one-time initialization of the vsys pin.  Used internally when necessary."""
        if (self._vsys_pin is None):
            self._vsys_pin = ADC(29)

    def turn_led_on(self):
        """Turns the on-board LED on."""
        self.__init_led_pin()

        assert self._led_pin is not None
        self._led_pin.on()

    def turn_led_off(self):
        """Turns the on-board LED off."""
        self.__init_led_pin()

        assert self._led_pin is not None
        self._led_pin.off()

    def read_temperature_volts(self) -> int:
        """Reads the on-board temperature sensor and returns the raw voltage value.  This measures the Vbe voltage of a biased bipolar diode, connected to the
        fifth ADC channel.  Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree."""
        self.__init_temp_pin()

        assert self._temperature_pin is not None
        return self._temperature_pin.read_u16()

    def read_temperature(self, unit: str = "f") -> float:
        """Reads the temperature in the units specified.
        :param unit: The unit to read the temperature as."""
        raw_value = self.read_temperature_volts()
        reading = raw_value * self._conversion_factor
        uom: str = 'f'

        if (unit is not None and (unit == 'f' or unit == 'F' or unit == 'c' or unit == 'C')):
            uom = unit

        base_temp = (27 - (reading - 0.706)/0.001721)

        if (uom.lower() == 'f'):
            return base_temp * 1.8 + 32
        else:
            return base_temp

    def read_input_voltage(self) -> float:
        """Reads the input voltage from VSYS."""
        self.__init_vsys_pin()

        assert self._vsys_pin is not None
        return self._vsys_pin.read_u16()

    def read_system_info(self) -> tuple[str, str, str]:
        """Reads system information (such as implementation, version, etc...)"""
        version_info = sys.implementation.version

        return (sys.implementation.name, '.'.join([str(version_info[0]), str(version_info[1]), str(version_info[2])]), sys.version)
