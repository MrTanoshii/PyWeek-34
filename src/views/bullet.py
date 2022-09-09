import arcade
import math

from src.audio import *
from src.enemy import *
from src.world import *


class Bullet(arcade.Sprite):
    """
    Game View

    ...

    Methods
    -------
    on_show()
        Show the main menu
    on_draw()
        Draw the main menu
    on_mouse_press(x: float, y: float, button: int, modifiers: int)
        Listen to mouse press event
    """

    bullet_list = arcade.SpriteList()

    def __init__(
        self, _angle: int, _center_x: int, _center_y: int, _dest_x: int, _dest_y: int
    ):
        # Inherit parent class
        super().__init__()

        Audio.play("shoot")
        start_x = _center_x
        start_y = _center_y

        dest_x = _dest_x
        dest_y = _dest_y

        self.speed = 1

        angle = math.atan2(dest_x - start_x, dest_y - start_y)
        self.angle = math.degrees(angle)

        self.speed_x = math.cos(math.radians(self.angle))
        self.speed_y = math.sin(math.radians(self.angle))
        self.texture = ":resources:images/space_shooter/laserBlue01.png"

    @classmethod
    def on_update(cls, delta_time: float = 1 / 60):
        for _b in cls.bullet_list:
            _b.center_x += math.cos(math.radians(_b.angle))
            _b.center_y += math.sin(math.radians(_b.angle))
