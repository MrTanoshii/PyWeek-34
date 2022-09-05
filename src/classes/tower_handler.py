import arcade

from interfases import Tower


class TowerHandler:
    """
    Interface for Tower handler classes.
    """

    def __init__(self) -> None:
        self.tower_list = arcade.SpriteList()

    def build_tower(self, tower: Tower):
        tower.center_x = 200
        tower.center_y = 200

        self.tower_list.append(tower)

    # def on_update(self, delta_time: float):
    #     pass

    def shoot(self, degree: float):
        pass
