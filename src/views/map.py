import arcade.gui

import src.const as C
from src.bullet import Bullet
from src.audio import *
from src.const import *
from src.gamedata import *
from src.gui import *
from src.world import *
from src.towers.tower_handler import TowerHandler, BuildException


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
        self.lives = Lives()
        self.score = Score()
        self.research = Research()

        self._load_map(tiled_name)

        self.notification_handler = NotificationHandler()
        self.gui = GUI(self.tower_handler, self.notification_handler, self.restart)

        # music default stopped
        Audio.stop(self.bgm_player)

    def _load_map(self, tiled_name: str, init_logic=True):
        self.tiled_name = tiled_name
        self.world = World.load(tiled_name)
        self._scene = arcade.Scene.from_tilemap(self.world.map)
        if init_logic:
            self.grid = Grid(int(self.world.height), int(self.world.width))
            self.enemy_handler = EnemyHandler(self.world, self.tiled_name)
            self.tower_handler = TowerHandler(self.world)
            self.bullets = Bullet(0, 0, 0, 0, "Missile.png")
            self.targeting = Targeting(self.world, self.enemy_handler)
        self.gold.reset()

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
        self.bullets.on_draw()  # Draw bullets
        self.tower_handler.on_draw()
        self.enemy_handler.on_draw()
        Bullet.on_draw()  # Draw bullets
        self.gui.manager.draw()
        self.gold.draw()
        self.score.draw()
        self.gui.draw_tower_selection()  # Draw tower selection
        self.lives.draw()
        self.gui.draw_tower_selection()
        self.notification_handler.draw()

    def on_update(self, delta_time: float):
        self.gui.manager.on_update(delta_time)

        self.gui.on_update()
        if self.gui.is_paused:  # update none if paused
            return

        self.enemy_handler.on_update(delta_time)
        self.gui.on_update()
        # Update bullets and check collision
        for bullet in self.bullets.bullet_list:
            bullet.on_update(
                delta_time=delta_time, enemy_list=self.enemy_handler.enemy_list
            )
        self.notification_handler.update(delta_time)
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

        Audio.on_update(delta_time)

        # Start new bgm if there is no current one and audio is not muted
        if (
            self.bgm_player is not None
            and not self.bgm_player.playing
            and not Audio.is_muted
        ):
            self.bgm_player = Audio.play_random(["bgm_1", "bgm_2"])

    def handle_tower(self, row: int, column: int, x: int, y: int):
        # Check if there is tower in the grid already
        if base_tower := self.grid.grid[row][column]["base_tower"]:  # if there's tower
            if self.tower_handler.is_removing:
                self.remove_tower(row, column)
                return

            self.tower_handler.select_tower(base_tower)
            if self.grid.grid[row][column]["tower"]:
                self.tower_handler.select_tower(self.grid.grid[row][column]["tower"])
            if C.DEBUG.MAP:
                print(f"Tower Clicked at: {row}, {column}")
            if C.DEBUG.TOWER:
                print(self.tower_handler.selected_type)
            # check if that tower already exist at that grid
            if self.is_tower_already_in(row, column):
                self.notification_handler.create(
                    f"You already have {self.tower_handler.selected_type['label']} on this grid",
                    x,
                    y,
                    (255, 0, 0),
                )
                return
            if (
                self.tower_handler.selected_type["name"] == C.TOWERS.BASE_TOWER["name"]
                and self.grid.grid[row][column]["base_tower"] is not None
            ):
                self.notification_handler.create(
                    f"You already have {self.tower_handler.selected_type['label']} on this grid",
                    x,
                    y,
                    (255, 0, 0),
                )
                return
            # Try to upgrade / level up tower
            if new_tower := self.tower_handler.buy_tower(
                row,
                column,
                tower_type=self.tower_handler.selected_type,
            ):  # if it's possible to build one
                self.grid.grid[row][column]["tower"] = new_tower

        # Check if there is tower in the nearby grids blocking new tower
        elif towers_around := self.grid.get_towers_around(
            row,
            column,
            (
                C.TOWERS.BASE_TOWER["size_tiles"] - 1
            ),  # -1 for finding intersections with another towers
        ):
            if self.tower_handler.is_removing:
                row_to_delete, column_to_delete = self.grid.get_cell(
                    towers_around[0].center_x, towers_around[0].center_y
                )
                self.remove_tower(row_to_delete, column_to_delete)
                return

            if C.DEBUG.MAP:
                print(f"Tower blocking at: {row}, {column}")
            self.notification_handler.create(
                f"Can't build here, another tower blocking",
                x,
                y,
                (255, 0, 0),
            )
            self.tower_handler.select_tower(towers_around[0])
        else:
            if self.tower_handler.is_removing:
                return

            # check if that tower already exist at that grid
            if self.is_base_tower_already_in(row, column):
                self.notification_handler.create(
                    f"You already have {self.tower_handler.selected_type['label']} on this grid",
                    x,
                    y,
                    (255, 0, 0),
                )
                return

            if self.grid.grid[row][column]["base_tower"] is None:
                if (
                    self.tower_handler.selected_type["name"]
                    == C.TOWERS.BASE_TOWER["name"]
                ):

                    # Add new tower foundation / base tower
                    if new_tower := self.tower_handler.buy_tower(
                        row,
                        column,
                        tower_type=C.TOWERS.BASE_TOWER,
                    ):  # if it's possible to build one
                        self.grid.grid[row][column]["base_tower"] = new_tower

                    if C.DEBUG.MAP:
                        print(f"Creating base at: {row}, {column}")
                else:
                    self.notification_handler.create(
                        f"You need to build {C.TOWERS.BASE_TOWER['label']} first",
                        x,
                        y,
                        (255, 0, 0),
                    )

        if C.DEBUG.MAP:
            print(f"Cell at [{row}, {column}] contains {self.grid.grid[row][column]}")

    def is_tower_already_in(self, row, column):
        current_tower = self.grid.grid[row][column]["tower"]
        if current_tower is None:
            return False
        return True

    def is_base_tower_already_in(self, row, column):
        current_tower = self.grid.grid[row][column]["base_tower"]
        if current_tower is None:
            return False
        return True

    def on_mouse_press(self, x, y, button, modifiers):
        """Use a mouse press to advance to the 'game' view."""
        if self.gui.is_paused:
            return

        current_cell_row, current_cell_column = self.grid.get_cell(x, y)
        if self.gui.manager.on_mouse_press(x, y, button, modifiers):
            return
        try:
            self.handle_tower(current_cell_row, current_cell_column, x, y)
        except BuildException as e:
            self.notification_handler.create(e.message, x, y, e.color)

    def on_mouse_motion(self, x, y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        if self.gui.is_paused:
            return

        self.grid.on_hover(x, y)

        self.tower_handler.draw_radius_(
            x, y, self.tower_handler.selected_type["radius"]
        )

    def on_key_press(self, symbol, _modifiers):
        """Called whenever a key is pressed."""

        # handle gui keyboard shortcuts
        self.gui.on_key_press(symbol, _modifiers)

        # handle keyboard shortcuts in
        self.gui.on_key_press(symbol, _modifiers)

        # Quicksave | F5
        if symbol == arcade.key.F5:
            pass
            # GameData.write_data()  # not in final version
        # Quickload | F6
        elif symbol == arcade.key.F6:
            pass
            # GameData.load_data()  # not in final version
        # Select tower deletion | R, Delete
        elif symbol == arcade.key.R or symbol == arcade.key.DELETE:
            self.tower_handler.select_tower_type(C.TOWERS.REMOVE_TOWER)
        # Stop music | M
        elif symbol == arcade.key.M:
            Audio.toggle_mute()
        elif symbol == arcade.key.S:
            self.enemy_handler.send_wave(*C.Waves.wave_1_1())  # TODO: change this
        # Reduce master volume | -
        elif symbol == arcade.key.MINUS or symbol == arcade.key.NUM_SUBTRACT:
            Audio.decrease_volume()
        # Increase master volume | +, =
        elif (
            symbol == arcade.key.PLUS
            or symbol == arcade.key.NUM_ADD
            or symbol == arcade.key.EQUAL
        ):
            Audio.increase_volume()
        # Cheat, add gold | I
        elif symbol == arcade.key.I:
            Gold.increment(C.RESOURCES.CHEAT_GOLD_INCREMENT)
        # Cheat, add lives | O
        elif symbol == arcade.key.O:
            Lives.increment(C.RESOURCES.CHEAT_LIVES_INCREMENT)

    def remove_tower(self, row: int, column: int):
        tower = self.grid.grid[row][column]["tower"]
        base_tower = self.grid.grid[row][column]["base_tower"]
        refund = 0
        if tower:
            refund += tower.gold_cost
        if base_tower:
            refund += base_tower.gold_cost
        Gold().increment(refund)
        self.grid.grid[row][column]["tower"] = None
        self.grid.grid[row][column]["base_tower"] = None
        self.tower_handler.select_tower(None)

    def restart(self):
        Gold.reset()
        Research.reset()
        Lives.reset()
        Audio.stop_all_sounds()
        self.window.show_view(MapView(self.tiled_name, self.label))
