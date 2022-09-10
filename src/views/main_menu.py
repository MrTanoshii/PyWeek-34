from itertools import islice


import arcade.gui
from src.gui.preview import Preview
from src.views import MapView
import src.const as C


class MainMenuView(arcade.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.levels_box = arcade.gui.UIBoxLayout()  # grid layout

        for row in self.get_levels():
            self.row_box = arcade.gui.UIBoxLayout(vertical=False)
            for label, map_name in row:
                if map_name in C.MENU.SECRET_LEVELS:
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
        self.manager.draw()
