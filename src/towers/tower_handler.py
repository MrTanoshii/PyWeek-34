import math
from typing import Optional
import arcade

import src.const as C
from src.bullet import Bullet
from src.enemy import *
from src.resources import *
from src.towers import Tower
from src.world import World


class BuildException(ValueError):
    def __init__(self, message: str, color: arcade.Color, *args):
        self.message = message
        self.color = color
        super().__init__(*args)


class TowerHandler:
    """
    Handling all towers logic
    """

    def __init__(self, world: World) -> None:
        self.selected_type: dict = C.TOWERS.BASE_TOWER
        self.selected_tower: Optional[Tower] = None
        self.world = world

    @property
    def is_removing(self):
        return self.selected_type == C.TOWERS.REMOVE_TOWER

    @staticmethod
    def build_tower(tower_type: dict) -> Tower:
        return Tower(tower_type)

    def buy_tower(self, row: int, column: int, tower_type: dict) -> Optional[Tower]:
        # Check for illegal placings
        if not self.world.is_fitting_borders(
            row, column, tower_type["size_tiles"]
        ):  # checking if tower doesn't go beyond the window borders
            if C.DEBUG.MAP:
                print(
                    f"{C.BCOLORS.WARNING}Warning: Tower cannot be placed outside window. {C.BCOLORS.ENDC}"
                )
            raise BuildException(
                "Can't be built here", C.NOTIFICATIONS.CANT_BUILT_COLOR
            )

        if self.world.is_tile_overlapping(
            row, column, tower_type["size_tiles"]
        ):  # isn't placed on a road
            if C.DEBUG.MAP:
                print(
                    f"{C.BCOLORS.WARNING}Warning: Tower cannot be placed on road. {C.BCOLORS.ENDC}"
                )
            raise BuildException(
                "Can't be built here", C.NOTIFICATIONS.CANT_BUILT_COLOR
            )

        if Gold.get() - tower_type["gold_cost"] < 0:  # checking gold
            if C.DEBUG.MAP:
                print(
                    f"{C.BCOLORS.WARNING}Warning: Not enough gold for new tower, "
                    f"You need {(Gold.get() - tower_type['gold_cost']) * -1} more gold. {C.BCOLORS.ENDC}"
                )
            raise BuildException(
                f"You need {(Gold.get() - tower_type['gold_cost']) * -1} more gold to build it",
                C.NOTIFICATIONS.NOT_ENOUGH_GOLD,
            )

        # Check for FOUNDATION tower
        tower = self.build_tower(tower_type)
        if tower_type == C.TOWERS.BASE_TOWER:
            tower.width = C.GRID.WIDTH * tower.size_tiles
            tower.height = C.GRID.WIDTH * tower.size_tiles
        tower.center_y = (row + 1) * C.GRID.WIDTH
        tower.center_x = (column + 1) * C.GRID.HEIGHT

        Gold.increment(-tower.gold_cost)
        self.selected_tower = tower

        return tower

    def select_tower(self, tower: Tower):
        self.selected_tower = tower

    def select_tower_type(self, tower_type: dict):
        self.selected_type = tower_type

    def shoot(self, tower: Tower, enemy: Enemy):
        if tower.cooldown <= 0:
            # if enemy.flying:
            #     enemy.take_damage(tower.damage_air)
            # else:
            #     enemy.take_damage(tower.damage_ground)
            tower.cooldown = tower.attack_cooldown_sec

            bullet = Bullet(
                math.radians(tower.angle + 90),  # get tower rotation as radians
                tower.center_x,
                tower.center_y,
            )
            bullet.damage_ground = tower.damage_ground
            Bullet.bullet_list.append(bullet)
            bullet.play_sound()
            # TODO: splash damage

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
