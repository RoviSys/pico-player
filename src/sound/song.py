class Song:
    """Class used to store a song for playing."""

    _notes: list[tuple[str, int]]

    def __init__(self):
        """Initializes a new instance of the Song class."""
        self._notes = []
