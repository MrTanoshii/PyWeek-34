import random

import arcade
import math
import src.const as C
from src.resources import *


class Enemy(arcade.Sprite):
    def __init__(
        self,
        position_list: list,
        image: str,
        scale: float = 1,
        hp: int = 100,
        speed: float = 10,
        gold_drop: int = 0,
        flying: bool = False,
        boss: bool = False,
        wobble: list[int] = [0, 0],
    ):

        image_path = C.EMEMY.BASEPATH / image
        super().__init__(image_path, scale)

        self.position_list = position_list
        self.hp_current = hp
        self.hp_max = hp
        self.speed = speed
        self.gold_drop = gold_drop
        self.flying = flying
        self.boss = boss
        self.wobble = wobble

        self.cur_position = 0
        self.poisoned = False
        self.poisoned_damage = 0  # per second damage
        self.poisoned_duration = 0
        self.slowed = False
        self.health_bar = HealthBar(self)

    def update(self, delta_time: float):
        if Lives.get() < 1:
            return
        if self.poisoned:
            self.take_damage(self.poisoned_damage * delta_time)
            self.poisoned_duration -= delta_time
            if self.poisoned_duration <= 0:
                self.poisoned_duration = 0
                self.poisoned_damage = 0
                self.poisoned = False

        start_x = self.center_x
        start_y = self.center_y

        dest_x = self.position_list[self.cur_position][0]
        dest_y = self.position_list[self.cur_position][1]

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        angle = math.atan2(y_diff, x_diff)

        distance = math.sqrt(
            (self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2
        )

        speed = self.speed
        if self.slowed and distance > self.speed * 0.5:
            self.color = (128, 128, 255, 128)
            speed /= 2
            self.slow_remaining -= delta_time
            if self.slow_remaining <= 0:
                self.slow_remaining = 0
                self.slowed = False
                self.color = (255, 255, 255, 255)

        change_x = math.cos(angle) * speed * delta_time
        change_y = math.sin(angle) * speed * delta_time

        wobble = self.wobble
        self.center_x += change_x + ((random.random() * wobble[0] * 2) - wobble[0])
        self.center_y += change_y + ((random.random() * wobble[1] * 2) - wobble[1])

        distance = math.sqrt(
            (self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2
        )

        if distance <= self.speed / 2:
            self.cur_position += 1
            if self.cur_position >= len(self.position_list):
                self.remove_from_sprite_lists()
                Lives.increment(-1)
                if self.boss:
                    if Lives > 0:
                        Lives.increment(-Lives.get())

    def take_damage(self, damage: float):
        self.hp_current -= damage
        if self.hp_current <= 0:
            self.remove_from_sprite_lists()
            Gold().increment(self.gold_drop)
            Score().increment(self.gold_drop)
            # TODO PLAY SOUND?  Maybe add death sounds?


class HealthBar(arcade.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.enemy = enemy
        self.width = enemy.width

    def on_draw(self):
        enemy_hp = self.enemy.hp_current / self.enemy.hp_max
        enemy_hp_removed = 1 - enemy_hp
        life_end = self.enemy.right - (
            (self.enemy.right - self.enemy.left) * enemy_hp_removed
        )
        below = self.enemy.bottom - 10
        arcade.draw_line(
            self.enemy.left,
            below,
            self.enemy.right,
            below,
            arcade.color.RED,
            line_width=5,
        )
        arcade.draw_line(
            self.enemy.left,
            below,
            life_end,
            below,
            arcade.color.GREEN,
            line_width=5,
        )
