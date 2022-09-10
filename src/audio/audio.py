import arcade
import pyglet
import random
from typing import Union

import src.const as C


class Audio:
    """Audio class."""

    sound_list = {}

    @classmethod
    def preload(cls):
        """Preload all sounds. To be called once."""

        for sound in C.AUDIO.MASTER_LIST:
            cls.sound_list[sound] = {}

            streaming = True
            if C.AUDIO.MASTER_LIST[sound]["type"] == "SFX":
                streaming = False

            cls.sound_list[sound]["sound"] = arcade.load_sound(
                C.AUDIO.BASE_PATH / C.AUDIO.MASTER_LIST[sound]["path"],
                streaming=streaming,
            )

            # Copy sound information from master list
            for key in C.AUDIO.MASTER_LIST[sound]:
                cls.sound_list[sound][key] = C.AUDIO.MASTER_LIST[sound][key]

    @classmethod
    def play(cls, sound: str) -> pyglet.media.Player:
        """Play a sound.

        Keyword arguments:
        sound: str -- The name of the sound to play.

        Returns:
        The sound stream player.
        """

        if sound in cls.sound_list:
            sound_stream_player = arcade.play_sound(
                cls.sound_list[sound]["sound"],
                max(  # Ensure value is 0 or above
                    min(  # Ensure value is MASTER VOLUME or below, considers sound type volume
                        cls.sound_list[sound]["gain"]
                        + C.AUDIO.VOLUME[
                            cls.sound_list[sound]["type"]
                        ],  # Apply gain to sound type volume
                        C.AUDIO.VOLUME["MASTER"]
                        * C.AUDIO.VOLUME[cls.sound_list[sound]["type"]],
                    ),
                    0,
                ),
                looping=cls.sound_list[sound]["loop"],
            )
            cls.sound_list[sound][
                "stream_player"
            ] = sound_stream_player  # Remember the last sound stream player
            return sound_stream_player
        else:
            raise ValueError(f"Sound {sound} not found.")

    @classmethod
    def play_random(cls, sound_list: list) -> pyglet.media.Player:
        """Play a random sound from a list.

        Keyword arguments:
        sound_list: list -- The list of sounds to play from.

        Returns:
        The sound stream player.
        """

        rand_index = random.randint(0, len(sound_list) - 1)
        return cls.play(sound_list[rand_index])

    @classmethod
    def stop(cls, sound: Union[str, pyglet.media.Player]):
        """Stop a currently playing sound or sound stream player.

        Keyword arguments:
        sound: str -- The name of the sound to stop.
        sound: pyglet.media.Player -- The sound stream player to stop.
        """

        if type(sound) is str:
            if sound in cls.sound_list:
                sound_stream = cls.sound_list[sound]["stream_player"]
                arcade.stop_sound(sound_stream)
            else:
                raise ValueError(f"Sound {sound} not found.")
        elif type(sound) is pyglet.media.Player:
            if sound.playing:
                arcade.stop_sound(sound)

    @classmethod
    def display_master_list(cls):
        """Display the master list of sounds."""

        print(cls.sound_list)

    @classmethod
    def reset(cls):
        C.AUDIO.VOLUME["MASTER"] = 1.0
