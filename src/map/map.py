import arcade
from interfases import Tower
from interfases import TowerHandler


class MapView(arcade.View):
    def __init__(self, tiled_name: str, label: str):
        # Inherit parent class
        super().__init__()
        self.tiled_name = tiled_name
        self.label = label
        self.enemy_handler = None  # TODO
        self.tower_handler = TowerHandler()
        self.gold = None  # TODO
        self.research = None  # TODO

        self._tile_map = arcade.load_tilemap(f"../resources/maps/{tiled_name}")
        self._scene = arcade.Scene.from_tilemap(self._tile_map)
        self._paths = self._tile_map.get_tilemap_layer("paths")

        anti_air_tower = Tower(
            name="anti-air-1",
            label="Anti Air Tower",
            radius=6,
            damage_air=30,
        )
        self.tower_handler.build_tower(anti_air_tower)

    def on_update(self, delta_time: int):
        self.draw()
        self.tower_handler.tower_list[0].center_x += 1

    def draw(self):
        self._scene.draw()
        self.tower_handler.tower_list.draw()
