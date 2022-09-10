import arcade
import arcade.gui

import src.const as C
from bullet import Bullet
from src.audio import *
from src.const import *
from src.enemy import *
from src.gamedata import *
from src.gui import *
from src.resources import *
from src.towers import *
from src.world import *


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
        Audio.preload()
        self.bgm_player = Audio.play_random(["bgm_1", "bgm_2"])

        self.tiled_name = tiled_name
        self.label = label

        self.gold = Gold()
        self.research = Research()

        self._load_map(tiled_name)
        self.gui = GUI(self.tower_handler)

    def _load_map(self, tiled_name: str, init_logic=True):
        self.tiled_name = tiled_name
        self.world = World.load(tiled_name)
        self._scene = arcade.Scene.from_tilemap(self.world.map)
        if init_logic:
            self.grid = Grid(int(self.world.height), int(self.world.width))
            self.enemy_handler = EnemyHandler(self.world)
            self.tower_handler = TowerHandler(self.world)
            self.targeting = Targeting(self.world, self.enemy_handler)

    def reload_map(self):
        self._load_map(self.tiled_name, init_logic=False)

    def on_resize(self, _width: int, _height: int):
        self.reload_map()
        self.grid.set_size(int(self.world.height), int(self.world.width))

    def on_show(self):
        """Called when switching to this view."""
        arcade.set_background_color(C.VIEWS.BACKGROUND_COLOR)

    def on_draw(self):
        """Draw the map view."""
        self._scene.draw()
        self.grid.on_draw()
        self.tower_handler.on_draw()
        self.enemy_handler.on_draw()
        self.gui.manager.draw()
        self.gold.draw()
        self.gui.draw_tower_selection()  # Draw tower selection

    def on_update(self, delta_time: float):
        self.gui.manager.on_update(delta_time)
        self.enemy_handler.on_update(delta_time)
        self.gui.on_update()
        Bullet.on_update(delta_time)  # Update bullets
        rows = self.grid.rows_count
        columns = self.grid.columns_count
        for row in range(rows):
            for column in range(columns):
                # get tower object from grid cell
                tower = self.grid.grid[row][column]["tower"]

                if not tower:
                    continue
                if tower.cooldown > 0:
                    tower.cooldown -= delta_time
                target = self.targeting.get_single_target(
                    tower, C.TARGETING.closest_target, C.TARGETING.ground_target
                )  # TODO: add checking for splash tower
                if target:
                    tower.angle = self.targeting.get_angle(tower, target)
                    self.tower_handler.shoot(tower, target)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        current_cell_row, current_cell_column = self.grid.get_cell(_x, _y)
        if self.gui.manager.on_mouse_press(_x, _y, _button, _modifiers):
            return

        # Check if there is tower in the grid already
        if base_tower := self.grid.grid[current_cell_row][current_cell_column][
            "base_tower"
        ]:  # if there's tower
            if self.tower_handler.is_removing:
                self.remove_tower(current_cell_row, current_cell_column)
                return

            self.tower_handler.select_tower(base_tower)
            if C.DEBUG.MAP:
                print(f"Tower Clicked at: {current_cell_row}, {current_cell_column}")
            print(self.tower_handler.selected_type)
            # Try to upgrade / level up tower
            if new_tower := self.tower_handler.buy_tower(
                current_cell_row,
                current_cell_column,
                tower_type=self.tower_handler.selected_type,
            ):  # if it's possible to build one
                self.grid.grid[current_cell_row][current_cell_column][
                    "tower"
                ] = new_tower

        # Check if there is tower in the nearby grids blocking new tower
        elif towers_around := self.grid.get_towers_around(
            current_cell_row,
            current_cell_column,
            (
                C.TOWERS.BASE_TOWER["size_tiles"] - 1
            ),  # -1 for finding intersections with another towers
        ):
            if self.tower_handler.is_removing:
                row_to_delete, column_to_delete = self.grid.get_cell(
                    towers_around[0].center_x, towers_around[0].center_y
                )  # kurwa
                self.remove_tower(row_to_delete, column_to_delete)
                return

            if C.DEBUG.MAP:
                print(f"Tower blocking at: {current_cell_row}, {current_cell_column}")
            self.tower_handler.select_tower(towers_around[0])
        else:
            if self.tower_handler.is_removing:
                return

            # Add new tower foundation / base tower
            if new_tower := self.tower_handler.buy_tower(
                current_cell_row,
                current_cell_column,
                tower_type=C.TOWERS.BASE_TOWER,
            ):  # if it's possible to build one
                self.grid.grid[current_cell_row][current_cell_column][
                    "base_tower"
                ] = new_tower

            if C.DEBUG.MAP:
                print(f"Creating base at: {current_cell_row}, {current_cell_column}")

        if C.DEBUG.MAP:
            print(
                f"Cell at [{current_cell_row}, {current_cell_column}] contains "
                f"{self.grid.grid[current_cell_row][current_cell_column]}"
            )

    def on_mouse_motion(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        # save_data.GameData.read_data()
        # self.window.show_view(MapView())
        self.grid.on_hover(_x, _y)

    def on_key_press(self, symbol, _modifiers):
        """Called whenever a key is pressed."""

        self.gui.on_key_press(symbol, _modifiers)

        # Quicksave | F5
        if symbol == arcade.key.F5:
            GameData.write_data()
        # Quickload | F6
        elif symbol == arcade.key.F6:
            GameData.load_data()
        # Reset Grids | R
        elif symbol == arcade.key.R:  # why? there are some bugs with it
            self.grid = Grid(int(self.world.height), int(self.world.width))
            self.gold.set(C.RESOURCES.DEFAULT_GOLD)
        # Stop music | M
        elif symbol == arcade.key.M:
            if self.bgm_player is not None:
                Audio.stop(self.bgm_player)
                self.bgm_player = None
            else:
                self.bgm_player = Audio.play_random(["bgm_1", "bgm_2"])
        elif symbol == arcade.key.S:
            self.enemy_handler.send_wave(*C.Waves.wave_1_1())  # TODO: change this

    def remove_tower(self, row: int, column: int):
        self.grid.grid[row][column]["tower"] = None
        self.grid.grid[row][column]["base_tower"] = None
        self.tower_handler.select_tower(None)
