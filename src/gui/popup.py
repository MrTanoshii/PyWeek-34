from typing import Callable

import arcade.gui
import src.const as C


class Popup(arcade.gui.UIBoxLayout):
    def __init__(
        self,
        text: str,
        restart_func: Callable[[], None],
        back_to_menu_func: Callable[[], None],
    ):
        self.restart_func = restart_func
        self.back_to_menu_func = back_to_menu_func
        super().__init__(vertical=True)

        self.add(
            arcade.gui.UILabel(text=text, font_size=28)
            .with_background(
                arcade.Texture.create_filled(
                    "popup_background", (1, 1), C.GUI.POPUP_TEXT_COLOR
                ),
                C.GUI.PADDING,
                C.GUI.PADDING * 2 + 1,  # pretty weird
                C.GUI.PADDING,
                C.GUI.PADDING * 2,
            )
            .with_space_around(bottom=C.GUI.PADDING)
        )

        restart_button = arcade.gui.UIFlatButton(text="Restart")

        @restart_button.event("on_click")
        def restart(_e):
            self.restart_func()

        self.add(restart_button.with_space_around(bottom=C.GUI.PADDING))

        back_button = arcade.gui.UIFlatButton(text="Back to menu")

        @back_button.event("on_click")
        def back(_e):
            self.back_to_menu_func()

        self.add(back_button.with_space_around(bottom=C.GUI.PADDING))

    @classmethod
    def create(
        cls,
        text: str,
        restart_func: Callable[[], None],
        back_to_menu_func: Callable[[], None],
    ) -> arcade.gui.UIWidget:
        return Popup(
            text,
            restart_func=restart_func,
            back_to_menu_func=back_to_menu_func,
        ).center_on_screen()
