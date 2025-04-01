from sound import (Song)


class SoundProvider:
    """Type that is used to drive playing songs via a sound driver."""

    _sound_driver: object

    def __init__(self, sound_driver):
        """Initializes a new instance of the SoundProvider class.
        :param sound_driver: The driver used to output sound info."""
        self._sound_driver = sound_driver

    def play_song(self, song: Song):
        """Plays the given song.
        :param song: The song to play."""

    def stop_sound(self):
        """Stops all sound currently playing on this provider."""
