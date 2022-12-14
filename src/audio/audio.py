import arcade
import pyglet
import random
from typing import Union
from copy import deepcopy

import src.const as C


class Audio:
    """Audio class."""

    sound_dict = {}
    currently_playing_dict = {}

    master_volume = C.AUDIO.VOLUME["MASTER"]
    is_muted = False

    @classmethod
    def preload(cls):
        """Preload all sounds. To be called once."""

        for sound in C.AUDIO.MASTER_LIST:
            cls.sound_dict[sound] = {}

            streaming = True
            if C.AUDIO.MASTER_LIST[sound]["type"] == "SFX":
                streaming = False

            cls.sound_dict[sound]["sound"] = arcade.load_sound(
                C.AUDIO.BASE_PATH / C.AUDIO.MASTER_LIST[sound]["path"],
                streaming=streaming,
            )

            # Copy sound information from master list
            for key in C.AUDIO.MASTER_LIST[sound]:
                cls.sound_dict[sound][key] = C.AUDIO.MASTER_LIST[sound][key]

    @classmethod
    def play(cls, sound: str) -> pyglet.media.Player:
        """Play a sound.

        Keyword arguments:
        sound: str -- The name of the sound to play.

        Returns:
        The sound stream player.
        """

        if cls.is_muted:
            return None

        if sound in cls.sound_dict:
            # if sound == "shoot" and "shoot" in cls.currently_playing_dict:
            #     print(123)
            #     return None
            sound_stream_player = arcade.play_sound(
                cls.sound_dict[sound]["sound"],
                max(  # Ensure value is 0 or above
                    min(  # Ensure value is MASTER VOLUME or below, considers sound type volume
                        cls.sound_dict[sound]["gain"]
                        + C.AUDIO.VOLUME[
                            cls.sound_dict[sound]["type"]
                        ],  # Apply gain to sound type volume
                        cls.master_volume
                        * C.AUDIO.VOLUME[cls.sound_dict[sound]["type"]],
                    ),
                    0,
                ),
                looping=cls.sound_dict[sound]["loop"],
            )

            # Remember the last sound stream player
            cls.sound_dict[sound]["stream_player"] = sound_stream_player

            if sound not in cls.currently_playing_dict:
                cls.currently_playing_dict[sound] = []

            # limit same sounds playing
            if len(cls.currently_playing_dict[sound]) >= C.AUDIO.SAME_SOUND_MAX:
                return None

            cls.currently_playing_dict[sound].append(
                {
                    "sound_stream": sound_stream_player,
                    "gain": cls.sound_dict[sound]["gain"],
                    "type": cls.sound_dict[sound]["type"],
                }
            )

            return sound_stream_player
        else:
            raise ValueError(f"Sound {sound} not found.")

    @classmethod
    def play_random(cls, sound_dict: list) -> pyglet.media.Player:
        """Play a random sound from a list.

        Keyword arguments:
        sound_dict: list -- The list of sounds to play from.

        Returns:
        The sound stream player.
        """

        rand_index = random.randint(0, len(sound_dict) - 1)
        return cls.play(sound_dict[rand_index])

    @classmethod
    def stop(cls, sound: Union[str, pyglet.media.Player]):
        """Stop a currently playing sound or sound stream player.

        Keyword arguments:
        sound: str -- The name of the sound to stop.
        sound: pyglet.media.Player -- The sound stream player to stop.
        """

        if type(sound) is str:
            if sound in cls.sound_dict:
                sound_stream = cls.sound_dict[sound]["stream_player"]
                arcade.stop_sound(sound_stream)
            else:
                raise ValueError(f"Sound {sound} not found.")
        elif type(sound) is pyglet.media.Player:
            if sound.playing:
                arcade.stop_sound(sound)

    @classmethod
    def display_master_list(cls):
        """Display the master list of sounds."""

        print(cls.sound_dict)

    @classmethod
    def on_update(cls, _delta_time: float):
        """Update. Called on every frame.

        Keyword arguments:
        delta_time: float -- The time since the last update.
        """

        # Only keep sounds that are currently playing
        still_playing_dict = {}
        for sound_name in cls.currently_playing_dict:
            for sound in cls.currently_playing_dict[sound_name]:
                if sound["sound_stream"].playing:
                    if sound_name not in still_playing_dict:
                        still_playing_dict[sound_name] = []
                    still_playing_dict[sound_name].append(sound)
        cls.currently_playing_dict = still_playing_dict.copy()

    @classmethod
    def increase_volume(cls):
        """Increment the master volume."""

        new_volume = cls.master_volume + C.AUDIO.VOLUME_INCREMENT

        if new_volume >= C.AUDIO.VOLUME_MIN and new_volume <= C.AUDIO.VOLUME_MAX:
            cls.master_volume = new_volume

            for i in cls.currently_playing_dict:
                new_sound_volume = max(  # Ensure value is 0 or above
                    min(  # Ensure value is MASTER VOLUME or below, considers sound type volume
                        cls.currently_playing_dict[i]["gain"]
                        + C.AUDIO.VOLUME[
                            cls.currently_playing_dict[i]["type"]
                        ],  # Apply gain to sound type volume
                        cls.master_volume
                        * C.AUDIO.VOLUME[cls.currently_playing_dict[i]["type"]],
                    ),
                    0,
                )
                cls.currently_playing_dict[i]["sound_stream"].volume = new_sound_volume

    @classmethod
    def decrease_volume(cls):
        """Decrement the master volume."""

        # new_volume = cls.master_volume - C.AUDIO.VOLUME_INCREMENT

        # if new_volume >= C.AUDIO.VOLUME_MIN and new_volume <= C.AUDIO.VOLUME_MAX:
        #     cls.master_volume = new_volume
        #     for sound_stream in cls.currently_playing_list:
        #         sound_stream.volume = new_volume

        new_volume = cls.master_volume - C.AUDIO.VOLUME_INCREMENT

        if new_volume >= C.AUDIO.VOLUME_MIN and new_volume <= C.AUDIO.VOLUME_MAX:
            cls.master_volume = new_volume

            for i in cls.currently_playing_dict:
                new_sound_volume = max(  # Ensure value is 0 or above
                    min(  # Ensure value is MASTER VOLUME or below, considers sound type volume
                        cls.currently_playing_dict[i]["gain"]
                        + C.AUDIO.VOLUME[
                            cls.currently_playing_dict[i]["type"]
                        ],  # Apply gain to sound type volume
                        cls.master_volume
                        * C.AUDIO.VOLUME[cls.currently_playing_dict[i]["type"]],
                    ),
                    0,
                )
                cls.currently_playing_dict[i]["sound_stream"].volume = new_sound_volume

    @classmethod
    def stop_all_sounds(cls):
        """Stops all currently playing sound streams."""

        for sound_name in cls.currently_playing_dict:
            for sound in cls.currently_playing_dict[sound_name]:
                cls.stop(sound["sound_stream"])
        cls.currently_playing_dict = {}

    @classmethod
    def mute(cls):
        """Mute audio."""

        cls.is_muted = True
        cls.stop_all_sounds()

    @classmethod
    def unmute(cls):
        """Unmute audio."""

        cls.is_muted = False

    @classmethod
    def toggle_mute(cls):
        """Toggle mute audio."""

        cls.is_muted = not cls.is_muted
        cls.stop_all_sounds()
