import arcade

import const as C


class TowerHandler:
    """
    Handling all towers logic
    """

    def __init__(self) -> None:
        self.tower_list = arcade.SpriteList()
        self.selected = None

    def build_tower(self, tower_type: type):
        tower = tower_type(
            **{k: v for k, v in tower_type.__dict__.items() if not k.startswith("__")}
        )
        return tower

    def shoot(self, degree: float):
        pass

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        pass
