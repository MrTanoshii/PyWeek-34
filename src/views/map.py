import arcade
import src.const as C
from classes.grid import Grid
from classes.tower_handler import TowerHandler

from classes.gold import Gold
from classes.research import Research
from classes.gamedata import GameData
from classes.world import World
from src.const import towers


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

        self.gold = Gold()
        self.research = Research()
        self.gold.increment(towers.TOWERS.DEFAULT_TOWER.cost)

        self._load_map(tiled_name)
        self.grid = Grid(int(self.world.height), int(self.world.width))

        self.enemy_handler = None  # TODO
        self.tower_handler = TowerHandler(self.world)

    def _load_map(self, tiled_name: str):
        self.tiled_name = tiled_name
        self.world = World.load(tiled_name)
        self._scene = arcade.Scene.from_tilemap(self.world.map)

    def reload_map(self):
        self._load_map(self.tiled_name)

    def on_resize(self, width: int, height: int):
        self.reload_map()
        self.grid.set_size(int(self.world.height), int(self.world.width))

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
        current_cell_row, current_cell_column = self.grid.get_cell(_x, _y)

        if self.grid.grid[current_cell_row][current_cell_column]["tower"]:
            pass  # TODO: select tower for upgrade view
        else:
            if tower := self.tower_handler.buy_tower(
                current_cell_row, current_cell_column, self.gold
            ):
                self.grid.grid[current_cell_row][current_cell_column]["tower"] = tower
            else:
                pass  # TODO: not enough money message

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