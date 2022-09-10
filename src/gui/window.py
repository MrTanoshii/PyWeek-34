from abc import abstractmethod
from typing import List

import arcade.gui
import src.const as C


class Window(arcade.gui.UIMouseFilterMixin, arcade.gui.UIWidget):
    def __init__(self, **kwargs):
        self.map_view = kwargs.pop("map_view")
        super().__init__(**kwargs)
        self.v_box = arcade.gui.UIBoxLayout(
            vertical=True, space_between=C.GUI.BUTTONS_GAP
        )

        for button in self.get_buttons():
            self.v_box.add(button)
        self.add(
            self.v_box.center_on_screen().with_background(
                arcade.load_texture(C.GUI.MENU_BG),
                C.GUI.PADDING,
                C.GUI.PADDING,
                C.GUI.PADDING,
                C.GUI.PADDING,
            )
        )

    @classmethod
    def create(cls, map_view) -> arcade.gui.UIWidget:
        return cls(map_view=map_view).center_on_screen()

    @abstractmethod
    def get_buttons(self) -> List[arcade.gui.UIFlatButton]:
        """
        Get list of buttons to render
        """
        pass


class Menu(Window):
    def get_buttons(self):
        restart_button = arcade.gui.UIFlatButton(text="Restart")
        exit_game_button = arcade.gui.UIFlatButton(text="Exit Game")

        @restart_button.event("on_click")
        def restart(_e):
            self.map_view.restart()

        @exit_game_button.event("on_click")
        def exit_game(_e):
            arcade.exit()

        return [
            restart_button,
            exit_game_button,
        ]
