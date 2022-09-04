import arcade


class Map:
    def __init__(self, tiled_name: str, label: str):
        self.tiled_name = tiled_name
        self.label = label
        self.enemy_handler = None  # TODO
        self.tower_handler = None  # TODO
        self.gold = None  # TODO
        self.research = None  # TODO

        self._tile_map = arcade.load_tilemap(f"../resources/maps/{tiled_name}")
        self._scene = arcade.Scene.from_tilemap(self._tile_map)
        self._paths = self._tile_map.get_tilemap_layer("paths")

    def on_update(self, delta_time: int):
        pass

    def draw(self):
        self._scene.draw()
