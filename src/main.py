import arcade

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
    # icon = pyglet.image.load("src/resources/images/cursor.png")
    # window.set_icon(icon)

    map_view = MapView("test_map_5.json", "123")
    window.show_view(map_view)
    arcade.run()


if __name__ == "__main__":
    main()
