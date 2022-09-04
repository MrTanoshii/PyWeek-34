import arcade

from map import MapView


def main():
    window = arcade.Window(
        width=1024,
        height=720,
        title="Map demo",
        center_window=True,
        resizable=True
    )

    map_view = MapView("test_map_2.json", "label")
    window.show_view(map_view)
    arcade.run()


if __name__ == "__main__":
    main()
