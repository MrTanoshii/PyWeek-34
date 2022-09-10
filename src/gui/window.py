from abc import abstractmethod
from typing import List, Callable

import arcade.gui
import src.const as C


class Window(arcade.gui.UIMouseFilterMixin, arcade.gui.UIWidget):
    def __init__(self, **kwargs):
        self.restart_func = kwargs.pop("restart_func", None)
        self.toggle_pause_func = kwargs.pop("toggle_pause_func", None)
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
    def create(
        cls,
        restart_func: Callable[[], None],
        toggle_pause_func: Callable[[], None],
    ) -> "Window":
        if toggle_pause_func:
            toggle_pause_func()
        return cls(restart_func=restart_func, toggle_pause_func=toggle_pause_func)

    def close(self):
        if self.toggle_pause_func:
            self.toggle_pause_func()

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
            self.restart_func()

        @exit_game_button.event("on_click")
        def exit_game(_e):
            arcade.exit()

        return [
            restart_button,
            exit_game_button,
        ]
