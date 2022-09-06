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
        self.selected_type: type = C.TOWERS.DEFAULT_TOWER
        self.selected_tower: Optional[Tower] = None
        self.world = world

    @staticmethod
    def build_tower(tower_type: type) -> Tower:
        required_arguments = inspect.getfullargspec(tower_type.__init__).args
        tower = tower_type(
            **{
                k: v
                for k, v in tower_type.__dict__.items()
                if not k.startswith("__")
                and k in required_arguments  # remove static fields
            }
        )

        tower.texture = arcade.load_texture(C.RESOURCES / "towers" / tower.name)

        tower.width = C.GRID.WIDTH * tower.size_tiles
        tower.height = C.GRID.HEIGHT * tower.size_tiles
        tower.scale = C.SETTINGS.GLOBAL_SCALE
        return tower

    def buy_tower(self, row: int, column: int, gold: Gold) -> Optional[Tower]:
        if not self.selected_type:
            self.selected_type = C.TOWERS.DEFAULT_TOWER

        # TODO: check researches

        if not self.world.is_fitting_borders(
            row, column, self.selected_type.size_tiles
        ):  # checking if tower doesn't go beyond the window borders
            return

        if self.world.is_tile_overlapping(
            row, column, self.selected_type.size_tiles
        ):  # isn't placed on a road
            return  # TODO: placed on road message

        if gold.get() - self.selected_type.cost < 0:  # checking gold
            return  # TODO: not enough gold message
        tower = self.build_tower(self.selected_type)
        tower.center_y = (row + 1) * C.GRID.WIDTH
        tower.center_x = (column + 1) * C.GRID.HEIGHT

        gold.increment(-tower.cost)
        self.selected_tower = tower

        return tower

    def select_tower(self, tower: Tower):
        self.selected_tower = tower

    def shoot(self, degree: float):
        pass

    def draw_radius(self, tower: Tower):
        arcade.draw_circle_filled(
            tower.center_x,
            tower.center_y,
            tower.radius * self.world.tile_size,
            C.TOWERS.RADIUS_BG_COLOR,
        )

    def draw_selected(self):
        if self.selected_tower:
            arcade.draw_rectangle_outline(
                self.selected_tower.center_x,
                self.selected_tower.center_y,
                self.selected_tower.width,
                self.selected_tower.height,
                C.TOWERS.SELECTED_OUTLINE_COLOR,
            )  # draw rectangle around selected tower
            self.draw_radius(self.selected_tower)

    def on_draw(self):
        self.draw_selected()
