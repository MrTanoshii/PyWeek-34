from itertools import islice


import arcade.gui
from resources import Gold, Research, Lives
from src.gui.preview import Preview
from src.views import MapView
from src.gamedata import GameData
from src.world import World
import src.const as C


class MainMenuView(arcade.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        GameData.load_data()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.levels_box = arcade.gui.UIBoxLayout()  # grid layout
        self.bg = arcade.load_texture("resources/bg.png")

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=arcade.gui.UILabel(
                    text="Select the level", font_size=18
                ).with_space_around(top=C.GUI.PADDING),
                anchor_x="center_x",
                anchor_y="top",
            )
        )  # I don't speak london

        for row in self.get_levels():
            self.row_box = arcade.gui.UIBoxLayout(vertical=False)
            for label, map_name in row:
                if (
                    map_name in C.MENU.SECRET_LEVELS
                    and map_name not in World.completed_levels
                ):
                    continue
                level_button = Preview(map_name=map_name, label=label)

                level_button.event("on_click")(
                    self.create_on_click(map_name, label)
                )  # fuck js

                self.row_box.add(
                    level_button.with_space_around(
                        C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING
                    )
                )
            self.levels_box.add(self.row_box)

        self.manager.add(self.levels_box.center_on_screen())

    def create_on_click(self, map_name: str, label: str):
        def level_start_handler(_e):
            self.manager.disable()  # weird but ok
            Gold.reset()
            Research.reset()
            Lives.reset()
            self.window.show_view(MapView(f"{map_name}.json", label))

        return level_start_handler

    @staticmethod
    def get_levels():
        """
        part levels to nested list with each being C.MENU.LEVELS_IN_ROW in length
        """
        for i in range(0, len(C.MENU.LEVELS.items()), C.MENU.LEVELS_IN_ROW):
            yield list(islice(list(C.MENU.LEVELS.items()), i, i + C.MENU.LEVELS_IN_ROW))

    def on_update(self, delta_time: float):
        self.manager.on_update(delta_time)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.manager.on_mouse_press(x, y, button, modifiers)

    def on_draw(self):
        self.bg.draw_sized(
            C.SETTINGS.SCREEN_WIDTH / 2,
            C.SETTINGS.SCREEN_HEIGHT / 2,
            C.SETTINGS.SCREEN_WIDTH,
            C.SETTINGS.SCREEN_HEIGHT,
        )
        self.manager.draw()
