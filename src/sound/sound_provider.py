from song import (Song)
from sound_driver import (SoundDriver)


class SoundProvider:
    """Type that is used to drive playing songs via a sound driver."""

    _sound_driver: SoundDriver

    def __init__(self, sound_driver: SoundDriver):
        """Initializes a new instance of the SoundProvider class.
        :param sound_driver: The driver used to output sound info."""
        self._sound_driver = sound_driver

    def play_song(self, song: Song):
        """Plays the given song.
        :param song: The song to play."""
        for i in range(len(song.notes)):
            if (song.notes[i][0] == "P"):
                self._sound_driver.quiet(song.notes[i])
            else:
                print(song.notes[i])
                self._sound_driver.tone(song.notes[i])
        self.stop_sound()

    def stop_sound(self):
        """Stops all sound currently playing on this provider."""
        self._sound_driver.off()
