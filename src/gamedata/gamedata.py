import json

from src.resources import *
from src.world import World


class GameData:
    """GameData is the base class for handling game save data."""

    @classmethod
    def write_data(cls):
        return
        """Write the save data to a file."""
        with open("src/saveslot_1.json", "w", encoding="utf-8") as file:
            _data = json.dumps(
                {
                    "gold": Gold.get(),
                    "research": Research.get(),
                    "passed_levels": World.completed_levels,
                }
            )
            file.write(_data)

    @classmethod
    def load_data(cls):
        return
        """Load the save data from a file."""

        try:
            with open("src/saveslot_1.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("ERROR: Save data not found. Regenerating...")
            cls.reset_data()
            data = {}

        if data:
            cls.check_data(data, "gold", Gold)
            cls.check_data(data, "research", Research)
            cls.check_levels(data, "passed_levels")

    @classmethod
    def check_levels(cls, data: dict, key: str):
        return
        if type(data[key]) != list:
            print(f"ERROR: {key} wrong type. Regenerating...")
            World.completed_levels = []  # regenerating...
        else:
            try:
                World.completed_levels = data[key]
            except KeyError:
                cls.load_data()

    @classmethod
    def check_data(cls, data, key, static_class):
        return
        """Check the integrity of a game data key."""

        if type(data[key]) != int:
            print(f"ERROR: {key} wrong type. Regenerating...")
            static_class.reset()
        else:
            try:
                static_class.set(data[key])
            except KeyError:
                print(f"ERROR: {key} invalid. Regenerating...")
                static_class.reset()
                cls.load_data()

    @classmethod
    def reset_data(cls):
        return
        """Reset the save data."""
        Score.reset()
        Gold.reset()
        Research.reset()
        World.completed_levels = []
