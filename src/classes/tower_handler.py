import arcade

from .tower import Tower


class TowerHandler:
    """
    Handling all towers logic
    """

    def __init__(self) -> None:
        self.tower_list = arcade.SpriteList()

    def build_tower(self, tower_type: type):
        # if not issubclass(tower_type, Tower):
        #     raise TypeError(
        #         "towerType argument has to be a class inherited from classes.tower.Tower"
        #     )
        tower = tower_type(
            **{k: v for k, v in tower_type.__dict__.items() if not k.startswith("__")}
        )

        tower.center_x = 200
        tower.center_y = 200

        self.tower_list.append(tower)

    def shoot(self, degree: float):
        pass
