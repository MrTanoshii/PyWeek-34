import arcade
import arcade.gui

import src.const as C
from src.audio import *
from src.const import *
from src.enemy import *
from src.gamedata import *
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
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.h_box = arcade.gui.UIBoxLayout(vertical=False)

        # Game UI

        texture_star = arcade.load_texture(
            ":resources:onscreen_controls/flat_dark/key_round.png"
        )
        texture_a = arcade.load_texture(":resources:onscreen_controls/flat_dark/a.png")
        texture_key = arcade.load_texture(
            ":resources:onscreen_controls/flat_dark/star.png"
        )

        # New Tower Button
        ui_new_tower = arcade.gui.UITextureButton(texture=texture_a).with_space_around(
            20, 20, 20, 20
        )
        self.h_box.add(ui_new_tower)

        # New Tower Button
        ui_new_tower = arcade.gui.UITextureButton(
            texture=texture_star
        ).with_space_around(20, 20, 20, 20)
        self.h_box.add(ui_new_tower)

        # New Tower Button
        ui_new_tower = arcade.gui.UITextureButton(
            texture=texture_key
        ).with_space_around(20, 20, 20, 20)
        self.h_box.add(ui_new_tower)

        # Create a widget to hold the h_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.h_box, align_y=-300
            )
        )

    def _load_map(self, tiled_name: str, init_logic=True):
        self.tiled_name = tiled_name
        self.world = World.load(tiled_name)
        self._scene = arcade.Scene.from_tilemap(self.world.map)
        if init_logic:
            self.grid = Grid(int(self.world.height), int(self.world.width))
            self.enemy_handler = EnemyHandler(self.world)
            self.tower_handler = TowerHandler(self.world)

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
        # self.manager.draw()

    def on_update(self, delta_time: float):
        self.enemy_handler.on_update(delta_time)
        rows = self.grid.rows_count
        columns = self.grid.columns_count
        for row in range(rows):
            for column in range(columns):

                # get tower object from grid cell
                tower = self.grid.grid[row][column]["tower"]

                if not tower:
                    continue

                tower.angle += 1

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        current_cell_row, current_cell_column = self.grid.get_cell(_x, _y)

        # Check if there is tower in the grid already
        if tower := self.grid.grid[current_cell_row][current_cell_column][
            "base_tower"
        ]:  # if there's tower
            self.tower_handler.select_tower(tower)
            if C.DEBUG.MAP:
                print(f"Tower Clicked at: {current_cell_row}, {current_cell_column}")

            # Try to upgrade / level up tower
            if tower := self.tower_handler.buy_tower(
                current_cell_row,
                current_cell_column,
                self.gold,
                tower_type=TOWERS.MG_TOWER,
            ):  # if it's possible to build one
                self.grid.grid[current_cell_row][current_cell_column]["tower"] = tower

        # Check if there is tower in the nearby grids blocking new tower
        elif towers_around := self.grid.get_towers_around(
            current_cell_row,
            current_cell_column,
            (
                self.tower_handler.selected_type["size_tiles"] - 1
            ),  # -1 for finding intersections with another towers
        ):

            if C.DEBUG.MAP:
                print(f"Tower blocking at: {current_cell_row}, {current_cell_column}")
            self.tower_handler.select_tower(towers_around[0])
        else:

            # Add new tower foundation / base tower
            if tower := self.tower_handler.buy_tower(
                current_cell_row,
                current_cell_column,
                self.gold,
                tower_type=TOWERS.FOUNDATION,
            ):  # if it's possible to build one
                self.grid.grid[current_cell_row][current_cell_column][
                    "base_tower"
                ] = tower

            if C.DEBUG.MAP:
                print(f"Creating base at: {current_cell_row}, {current_cell_column}")

        if C.DEBUG.MAP:
            print(
                f"Cell at [{current_cell_row}, {current_cell_column}] contains {self.grid.grid[current_cell_row][current_cell_column]}"
            )

    def on_mouse_motion(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        # save_data.GameData.read_data()
        # self.window.show_view(MapView())
        self.grid.on_hover(_x, _y)

    def on_key_press(self, symbol, _modifiers):
        """Called whenever a key is pressed."""

        # Quicksave | F5
        if symbol == arcade.key.F5:
            GameData.write_data()
        # Quickload | F6
        elif symbol == arcade.key.F6:
            GameData.load_data()
        # Reset Grids | R
        elif symbol == arcade.key.R:
            self.grid = None
            self.grid = CLASSES.Grid(int(self.world.height), int(self.world.width))
        # Stop music | M
        elif symbol == arcade.key.M:
            if self.bgm_player is not None:
                Audio.stop(self.bgm_player)
                self.bgm_player = None
            else:
                self.bgm_player = Audio.play_random(["bgm_1", "bgm_2"])
