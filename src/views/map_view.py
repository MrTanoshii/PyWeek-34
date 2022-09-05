from random import random
import arcade
import src.const as C

from src.classes import *


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

    def __init__(self):
        # Inherit parent class
        super().__init__()

    def on_show(self):
        """Called when switching to this view."""
        arcade.set_background_color(C.VIEWS.BACKGROUND_COLOR)

    def on_draw(self):
        """Draw the map view."""

        # TODO: To remove this. It was for testing only.
        self.clear()
        arcade.draw_text(
            f"Gold {Gold.get()} Research {Research.get()}",
            arcade.get_window().width / 2,
            arcade.get_window().height / 2,
            arcade.color.BLACK,
            font_size=C.VIEWS.FONT_SIZE
            * 2
            * arcade.get_window().height
            / C.SETTINGS.SCREEN_HEIGHT,
            anchor_x="center",
        )

    def on_update(self, delta_time: float):
        # TODO: To remove this. It was for testing only.
        Gold.increment(1)
        Research.increment((random() * 10) - (random() * 10))

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        # save_data.GameData.read_data()
        self.window.show_view(MapView())

    def on_key_press(self, symbol, modifiers):
        """Called whenever a key is pressed."""

        # Quicksave | F5
        if symbol == arcade.key.F5:
            GameData.write_data()
        # Quickload | F6
        elif symbol == arcade.key.F6:
            GameData.load_data()
