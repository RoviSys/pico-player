MAX_INT: int = 65535
"""The maximum value for an integer (to simplify other constants that are specific in function but share the same value)."""
MAX_ADC: int = MAX_INT
"""The maximum voltage for analog-to-digital signals (10,000 mV in decimal notation)."""
MAX_FREQUENCY: int = MAX_INT
"""The maximum frequency for a Piezo Buzzer."""
MIN_FREQUENCY: int = 31
"""The minimum frequency for a Piezo Buzzer."""
PICO_ONBOARD_LED_PIN: int = 25
"""The pin number for the on-board LED for a Raspberry PI Pico (note that the Pico W uses a named pin called "LED")."""
