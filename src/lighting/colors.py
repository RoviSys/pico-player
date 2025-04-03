class Colors:
    """A class used to setup pre-defined LED colors.  Used mostly for convenience and readability."""
    BLACK: tuple[int, int, int] = (0, 0, 0)
    RED: tuple[int, int, int] = (255, 0, 0)
    ORANGE: tuple[int, int, int] = (200, 50, 0)
    YELLOW: tuple[int, int, int] = (255, 150, 0)
    GREEN: tuple[int, int, int] = (0, 255, 0)
    CYAN: tuple[int, int, int] = (0, 255, 255)
    BLUE: tuple[int, int, int] = (0, 0, 255)
    PURPLE: tuple[int, int, int] = (180, 0, 255)
    WHITE: tuple[int, int, int] = (255, 255, 255)
    PINK: tuple[int, int, int] = (230, 120, 80)

    @staticmethod
    def CUSTOM(red: int, green: int, blue: int) -> tuple[int, int, int]:
        """Use this method to define a custom RGB color for showing.  Note that not all LEDs will show the given color well (orange and brown are tricky).
        :param red: The amount of red (0 - 255).
        :param green: The amount of green (0 - 255).
        :param blue: The amount of blue (0 - 255)."""
        return (red, green, blue)
