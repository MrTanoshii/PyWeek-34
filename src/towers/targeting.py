import arcade
import math
from typing import List, Callable, Tuple, Optional
from src.enemy import EnemyHandler, Enemy
from src.world import World
from .tower import Tower


class Targeting:
    def __init__(self, world: World, enemy_handler: EnemyHandler):
        self.enemy_handler = enemy_handler
        self.world = world

    def find_in_radius(self, tower: Tower) -> List[Tuple[Enemy, float]]:
        radius = tower.radius * self.world.tile_size
        return list(
            filter(
                lambda x: x[1] <= radius,
                map(
                    lambda enemy: (
                        enemy,
                        arcade.get_distance_between_sprites(
                            tower, enemy
                        ),  # someone already did weird math
                    ),
                    self.enemy_handler.enemy_list,
                ),
            )
        )

    def get_many_targets(
        self,
        tower: Tower,
        filter_function: Callable[[Enemy], bool],
    ) -> List[Tuple[Enemy, float]]:
        return list(
            filter(
                lambda x: filter_function(x[0]),
                self.find_in_radius(tower),
            )
        )

    def get_single_target(
        self,
        tower: Tower,
        targeting_function: Callable[[List[Tuple[Enemy, float]]], Tuple[Enemy, float]],
        filter_function: Callable[[Enemy, float], bool],
    ) -> Optional[Enemy]:
        if enemies := self.get_many_targets(
            tower,
            filter_function,
        ):
            return targeting_function(enemies)[0]

    @staticmethod
    def get_angle(tower: Tower, enemy: Enemy) -> float:
        radians = math.atan2(
            tower.center_y - enemy.center_y,
            tower.center_x - enemy.center_x,
        )  # get angle from vector
        return radians * (180 / math.pi) + 90  # weird math; 90 because of trigonometry
