import arcade
import math
import src.const as C


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

        self.cur_position = 0
        self.poisoned = False
        self.poisoned_damage = 0
        self.poisoned_duration = 0
        self.slowed = False

    def update(self, delta_time: float):
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

        speed = min(self.speed, distance)
        if self.slowed and distance > self.speed * 0.5:
            speed /= 2

        change_x = math.cos(angle) * speed * delta_time
        change_y = math.sin(angle) * speed * delta_time

        self.center_x += change_x
        self.center_y += change_y

        distance = math.sqrt(
            (self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2
        )

        if distance <= self.speed:
            self.cur_position += 1
            if self.cur_position >= len(self.position_list):
                self.remove_from_sprite_lists()
                #TODO TAKE AWAY PLAYER LIFE
                if self.boss:
                    #TODO TAKE AWAY ALL REMAINING PLAYER LIVES
                    ...

    def takeDamage(self, damage: int):
        self.hp_current -= damage
        if self.hp_current < 0:
            self.remove_from_sprite_lists()
            # TODO PLAY SOUND?  Maybe add death sounds?