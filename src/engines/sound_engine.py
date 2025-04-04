from shared import (Logger, LogLevel)
from input import (Button)
from sound import (SoundProvider, SingleBuzzerDriver, Song)
import _thread


class SoundEngine:
    """Engine used to encapsulate logic for controlling sound and playback."""

    _sound_gpio: int
    _button_gpio: int
    _button_logger: Logger
    _sound_logger: Logger
    _button: Button
    _sound_provider: SoundProvider
    _should_stop: bool
    _song: Song

    def __init__(self, sound_gpio: int, button_gpio: int, interrupt, should_stop: bool):
        self._sound_gpio = sound_gpio
        self._button_gpio = button_gpio
        self._interrupt = interrupt

        self._button_logger = Logger('button', LogLevel.DEBUG)
        self._sound_logger = Logger('sound')
        self._should_stop = should_stop
        self._button = Button(self._button_logger, self._button_gpio, self._should_stop)
        sound_driver = SingleBuzzerDriver(self._sound_logger, self._sound_gpio)
        self._sound_provider = SoundProvider(sound_driver)


    def start_playback_listener(self, song: Song):
        self._song = song
        _thread.stack_size(8*1024)
        _thread.start_new_thread(self._button.listen, [self._trigger_song])
    
    def _trigger_song(self):
        self._play_song(self._song)
    
    def _play_song(self, song: Song):
        self._sound_provider.play_song(song)
        self._sound_provider.stop_sound()
        self.stop_playback_listener() # Play one time

    def stop_playback_listener(self):
        self._interrupt()
