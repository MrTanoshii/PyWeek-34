from abc import abstractmethod
from typing import List

import arcade.gui
import src.const as C


class Window(arcade.gui.UIMouseFilterMixin, arcade.gui.UIWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.v_box = arcade.gui.UIBoxLayout(
            vertical=True, space_between=C.GUI.BUTTONS_GAP
        )

        for button in self.get_buttons():
            self.v_box.add(button)
        self.add(self.v_box.center_on_screen())

    @classmethod
    def create(cls) -> arcade.gui.UIWidget:
        return (
            cls()
            .with_background(
                arcade.load_texture(C.GUI.MENU_BG),
                C.GUI.PADDING,
                C.GUI.PADDING,
                C.GUI.PADDING,
                C.GUI.PADDING,
            )
            .center_on_screen()
            .with_border()
        )

    @abstractmethod
    def get_buttons(self) -> List[arcade.gui.UIFlatButton]:
        """
        Get list of buttons to render
        """
        pass


class Menu(Window):
    def get_buttons(self):
        return [
            arcade.gui.UIFlatButton(text="btn1"),
            arcade.gui.UIFlatButton(text="btn2"),
        ]
