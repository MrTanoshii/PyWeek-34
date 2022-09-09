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
        self,
        _angle: float,
        _center_x: float,
        _center_y: float,
        _dest_x: float,
        _dest_y: float,
    ):
        # Inherit parent class
        super().__init__()

        Audio.play("shoot")

        self.center_x = _center_x
        self.center_y = _center_y

        dest_x = _dest_x
        dest_y = _dest_y

        self.speed = 1

        angle = math.atan2(dest_x - self.center_x, dest_y - self.center_y)
        self.angle = math.degrees(angle)

        self.change_x = math.cos(math.radians(self.angle))
        self.change_y = math.sin(math.radians(self.angle))
        self.texture = arcade.load_texture(
            ":resources:images/space_shooter/laserBlue01.png"
        )

    @classmethod
    def on_update(cls, delta_time: float):
        for _b in cls.bullet_list:
            # calculate how much x and y coordinates should be changed to move to right direction
            _b.center_x += _b.change_x
            _b.center_y += _b.change_y

    @classmethod
    def on_draw(cls):
        cls.bullet_list.draw()
