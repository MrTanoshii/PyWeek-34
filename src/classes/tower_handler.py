import arcade
import inspect
from typing import Optional

import const as C
from .tower import Tower
from .gold import Gold
from .world import World


class TowerHandler:
    """
    Handling all towers logic
    """

    def __init__(self, world: World) -> None:
        self.tower_list = arcade.SpriteList()
        self.selected: type = C.TOWERS.DEFAULT_TOWER
        self.world = world

    @staticmethod
    def build_tower(tower_type: type) -> Tower:
        required_arguments = inspect.getfullargspec(tower_type.__init__).args
        tower = tower_type(
            **{
                k: v
                for k, v in tower_type.__dict__.items()
                if not k.startswith("__") and k in required_arguments
            }
        )

        tower.texture = arcade.load_texture(C.RESOURCES / "towers" / tower.name)

        tower.width = C.GRID.WIDTH * tower.size_tiles
        tower.height = C.GRID.HEIGHT * tower.size_tiles
        tower.scale = C.SETTINGS.GLOBAL_SCALE
        return tower

    def buy_tower(self, row: int, column: int, gold: Gold) -> Optional[Tower]:
        if not self.selected:
            self.selected = C.TOWERS.DEFAULT_TOWER

        # TODO: check researches

        if self.world.is_tile_overlapping(
            row, column, self.selected.size_tiles
        ):  # isn't placed on a road
            return

        if gold.get() - self.selected.cost >= 0:  # is enough gold
            tower = self.build_tower(self.selected)
            tower.center_y = (row + 1) * C.GRID.WIDTH
            tower.center_x = (column + 1) * C.GRID.HEIGHT

            gold.increment(-tower.cost)

            return tower

    def shoot(self, degree: float):
        pass
