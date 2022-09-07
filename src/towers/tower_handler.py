import arcade
from typing import Optional

import src.const as C
from .tower import Tower
from src.resources import *
from src.world import *


class TowerHandler:
    """
    Handling all towers logic
    """

    def __init__(self, world: World) -> None:
        self.selected_type: dict = C.TOWERS.BASE_TOWER
        self.selected_tower: Optional[Tower] = None
        self.world = world

    @staticmethod
    def build_tower(tower_type: type) -> Tower:
        return Tower(tower_type)

    def buy_tower(self, row: int, column: int, gold: Gold) -> Optional[Tower]:
        if not self.selected_type:
            self.selected_type = C.TOWERS.BASE_TOWER

        # TODO: check researches

        if not self.world.is_fitting_borders(
            row, column, self.selected_type["size_tiles"]
        ):  # checking if tower doesn't go beyond the window borders
            return

        if self.world.is_tile_overlapping(
            row, column, self.selected_type["size_tiles"]
        ):  # isn't placed on a road
            return  # TODO: placed on road message

        if gold.get() - self.selected_type["gold_cost"] < 0:  # checking gold
            return  # TODO: not enough gold message
        tower = self.build_tower(self.selected_type)
        tower.center_y = (row + 1) * C.GRID.WIDTH
        tower.center_x = (column + 1) * C.GRID.HEIGHT

        gold.increment(-tower.gold_cost)
        gold.increment(-tower.research_cost)
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
