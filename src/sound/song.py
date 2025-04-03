class Song:
    """Class used to store a song for playing."""

    _notes: list[tuple[str, float, int]]
    """A collection of note tuples for the note (A4 for example), duration (in seconds), and volume (typically frequency but depends on the driver)"""

    def __init__(self, notes: list[tuple[str, float, int]]):
        """Initializes a new instance of the Song class.
        :param notes: The notes of the song to play"""
        self._notes = [] if notes is None else notes

    @property
    def notes(self) -> list[tuple[str, float, int]]:
        """Gets the notes of the song"""
        return self._notes
