import arcade
import pyglet

import src.const as C

from src.views import MapView


def main():
    """Main function."""

    window = arcade.Window(
        width=C.SETTINGS.SCREEN_WIDTH,
        height=C.SETTINGS.SCREEN_HEIGHT,
        title=C.SETTINGS.SCREEN_TITLE,
        center_window=C.SETTINGS.CENTER_WINDOW,
        resizable=C.SETTINGS.RESIZEABLE,
        fullscreen=C.SETTINGS.FULLSCREEN,
        style="borderless" if C.SETTINGS.FULLSCREEN_WINDOWED else None,
    )

    window.set_mouse_visible(C.SETTINGS.CURSOR_VISIBLE)
    # add icon to window
    icon = pyglet.image.load("resources/icon.png")
    window.set_icon(icon)

    map_view = MapView("draft_level_1.json", "Level 1")
    # map_view = MapView("draft_level_2.json", "Level 2")
    # map_view = MapView("draft_level_3.json", "Level 3")
    # map_view = MapView("draft_level_4.json", "Level 4")
    # map_view = MapView("draft_level_5.json", "Level 5")
    # map_view = MapView("draft_level_secret_duck.json", "Secret Level Duck")
    # map_view = MapView("draft_level_secret_turtle.json", "Secret Level Turtle")
    # map_view = MapView("draft_level_secret_penguin.json", "Secret Level Penguin")
    window.show_view(map_view)
    arcade.run()


if __name__ == "__main__":
    main()
