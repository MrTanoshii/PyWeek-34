from pathlib import Path

import arcade
import src.const as C
from src.const import towers

from src.classes import *


class MapView(arcade.View):
    """
    Game View

    ...

    Methods
    -------
    on_show()
        Show the main menu
    on_draw()
        Draw the main menu
    on_mouse_press(x: float, y: float, button: int, modifiers: int)
        Listen to mouse press event
    """

    def __init__(self, tiled_name: str, label: str):
        # Inherit parent class
        super().__init__()

        self.tiled_name = tiled_name
        self.label = label
        self.enemy_handler = None  # TODO
        self.tower_handler = TowerHandler()
        self.gold = None  # TODO
        self.research = None  # TODO

        self._tile_map = arcade.load_tilemap(
            Path("..") / "resources" / "maps" / tiled_name
        )
        self._scene = arcade.Scene.from_tilemap(self._tile_map)
        self._paths = self._tile_map.get_tilemap_layer("paths")

        self.tower_handler.build_tower(towers.AntiAirTower)

    def on_show(self):
        """Called when switching to this view."""
        arcade.set_background_color(C.VIEWS.BACKGROUND_COLOR)

    def on_draw(self):
        """Draw the map view."""
        self._scene.draw()
        self.tower_handler.tower_list.draw()

    def on_update(self, delta_time: float):
        self.tower_handler.tower_list[0].center_x += 1

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        # save_data.GameData.read_data()
        # self.window.show_view(MapView())

    def on_key_press(self, symbol, modifiers):
        """Called whenever a key is pressed."""

        # Quicksave | F5
        if symbol == arcade.key.F5:
            GameData.write_data()
        # Quickload | F6
        elif symbol == arcade.key.F6:
            GameData.load_data()
