from pathlib import Path

import arcade
import src.const as C
from classes.grid import Grid
from classes.tower import Tower
from classes.tower_handler import TowerHandler
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

        self._load_map(tiled_name)
        self._scene = arcade.Scene.from_tilemap(self._tile_map)
        self._paths = self._tile_map.get_tilemap_layer("paths")

        self.tower_handler.build_tower(towers.AntiAirTower)

        self.grid = Grid(int(self._tile_map.height), int(self._tile_map.width))

        self.selected_tower_size = 2

    def _load_map(self, tiled_name: str):
        self.tiled_name = tiled_name
        scale = 1.25 * arcade.get_window().height / 720
        self._tile_map = None
        self._tile_map = arcade.load_tilemap(
            rf"resources/maps/{tiled_name}", scaling=scale
        )
        self._scene = arcade.Scene.from_tilemap(self._tile_map)

    def reload_map(self):
        self._load_map(self.tiled_name)

    def on_resize(self, width: int, height: int):
        self.reload_map()
        self.grid.set_size(int(self._tile_map.height), int(self._tile_map.width))

    def on_show(self):
        """Called when switching to this view."""
        arcade.set_background_color(C.VIEWS.BACKGROUND_COLOR)

    def on_draw(self):
        """Draw the map view."""
        self._scene.draw()
        self.tower_handler.tower_list.draw()
        self.grid.on_draw()

    def on_update(self, delta_time: float):
        pass

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        self.tower_handler.on_mouse_press(_x, _y, _button, _modifiers)

        current_cell_row, current_cell_column = self.grid.get_cell(_x, _y)

        new_tower = self.tower_handler.build_tower(towers.AntiAirTower)
        new_tower.center_y = (current_cell_row + 1) * C.GRID.WIDTH
        new_tower.center_x = (current_cell_column + 1) * C.GRID.HEIGHT
        new_tower.scale = C.SETTINGS.GLOBAL_SCALE
        new_tower.width = C.GRID.WIDTH * self.selected_tower_size
        new_tower.height = C.GRID.HEIGHT * self.selected_tower_size

        self.grid.grid[current_cell_row][current_cell_column]["tower"] = new_tower

    def on_mouse_motion(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        # save_data.GameData.read_data()
        # self.window.show_view(MapView())
        self.grid.on_hover(_x, _y)

    def on_key_press(self, symbol, modifiers):
        """Called whenever a key is pressed."""

        # Quicksave | F5
        if symbol == arcade.key.F5:
            GameData.write_data()
        # Quickload | F6
        elif symbol == arcade.key.F6:
            GameData.load_data()
