import arcade
from pytiled_parser.tiled_object import Rectangle


class World:
    def __init__(self, tile_map: arcade.tilemap.TileMap):
        self.map = tile_map
        self.paths = tile_map.get_tilemap_layer("paths")
        self.roads = list(filter(lambda x: x.type == "road", self.objects))
        self.spawners = list(filter(lambda x: x.type == "spawners", self.objects))
        self.finishes = list(filter(lambda x: x.type == "finish", self.objects))

    @classmethod
    def load(cls, tiled_name: str) -> "World":
        scale = 1.25 * arcade.get_window().height / 720
        return cls(arcade.load_tilemap(rf"resources/maps/{tiled_name}", scaling=scale))

    @property
    def objects(self):
        return self.paths.tiled_objects

    @property
    def width(self):
        return self.map.width

    @property
    def height(self):
        return self.map.height

    @property
    def tile_size(self):
        return self.map.tile_width

    def screen_to_grid(self, x: float, y: float) -> [int, int]:
        return [x // self.tile_size, y // self.tile_size]

    def grid_to_tiled(self, row: int, column: int):
        """
        Tiled counts coordinates from top-left but arcade from bottom left
        """
        return [self.height - row - 1, column]  # weird math

    def is_cell_inside_object(self, row: int, column: int, obj: Rectangle) -> bool:
        row, column = self.grid_to_tiled(row, column)
        start_x, start_y = self.screen_to_grid(obj.coordinates.x, obj.coordinates.y)
        size_x, size_y = self.screen_to_grid(obj.size.width, obj.size.height)

        x = start_x <= column <= start_x + size_x - 1
        y = start_y <= row <= start_y + size_y - 1

        return x and y

    def is_cell_overlapping(self, row: int, column: int) -> bool:
        for obj in self.objects:
            if self.is_cell_inside_object(row, column, obj):
                return True
        return False

    def is_tile_overlapping(self, row: int, column: int, tile_size: int) -> bool:
        for i in range(tile_size):
            for j in range(tile_size):
                if self.is_cell_overlapping(row + i, column + j):
                    return True
        return False

    def is_fitting_borders(self, row: int, column: int, tile_size: int) -> bool:
        return (
            column + tile_size <= self.width
            and tile_size <= row + tile_size <= self.height
        )
