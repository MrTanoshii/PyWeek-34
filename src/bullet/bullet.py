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
    ):
        # Inherit parent class
        super().__init__()

        self.center_x = _center_x
        self.center_y = _center_y

        self.speed = 3

        angle = _angle
        self.angle = math.degrees(angle)

        self.change_x = math.cos(math.radians(self.angle))
        self.change_y = math.sin(math.radians(self.angle))
        self.texture = arcade.load_texture(
            ":resources:images/space_shooter/laserBlue01.png"
        )

    def on_update(self, delta_time: float, enemy_list):
        for bullet in self.bullet_list:
            # update bullet location
            bullet.center_x += bullet.change_x * self.speed
            bullet.center_y += bullet.change_y * self.speed

            # Check this bullet to see if it hit an enemy
            hit_list = arcade.check_for_collision_with_list(bullet, enemy_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every enemy we hit reduce health and remove if less than zero
            for enemy in hit_list:
                enemy.take_damage(bullet.damage_ground)
                break

    @classmethod
    def on_draw(cls):
        cls.bullet_list.draw()

    @classmethod
    def play_sound(cls):
        Audio.play("shoot")
