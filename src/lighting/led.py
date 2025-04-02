class LED:
    """Represents an individual LED instance."""
    _red: int
    _green: int
    _blue: int
    _name: str

    def __init__(self, name: str):
        """Initializes a new LED instance
        :param name: The name of the LED (for readability and debugging)"""
        self._red = 0
        self._green = 0
        self._blue = 0
        self._name = name

    def set_color(self, r: int, g: int, b: int):
        """Sets the rgb values of the LED.
        :param r: The red value (0 - 255).
        :param g: The green value (0 - 255).
        :param b: The blue value (0 - 255)."""
        self._red = r
        self._green = g
        self._blue = b

    @property
    def name(self) -> str:
        """Gets the name of the LED."""
        return self._name

    def current_color_rgb(self) -> tuple[int, int, int]:
        """Returns the RGB value of the LED as a tuple of integers."""
        return (self._red, self._green, self._blue)

    def current_color(self) -> int:
        """Returns the binary shifted color for display."""
        return (self._red<<16)+(self._green<<8)+self._blue
