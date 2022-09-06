import arcade
import math

class Enemy(arcade.Sprite):

    def __init__(self,
                 position_list,
                 image,
                 scale=1,
                 hp=100,
                 speed=10,
                 gold_drop=0,
                 armor_type=None,
                 flying=False,
                 boss=False
                 ):

        super().__init__(image, scale)

        self.position_list = position_list
        self.hp_current = hp
        self.hp_max = hp
        self.speed = speed
        self.armor_type = armor_type
        self.flying = flying
        self.boss = boss

        self.cur_position = 0
        self.poisoned = False
        self.slowed = False


    def update(self):

        start_x = self.center_x
        start_y = self.center_y

        dest_x = self.position_list[self.cur_position][0]
        dest_y = self.position_list[self.cur_position][1]

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        angle = math.atan2(y_diff, x_diff)

        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        speed = min(self.speed, distance)
        if self.slowed and distance > self.speed * .5:
            speed /= 2

        change_x = math.cos(angle) * speed
        change_y = math.sin(angle) * speed

        self.center_x += change_x
        self.center_y += change_y

        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        if distance <= self.speed:
            self.cur_position += 1
            if self.cur_position >= len(self.position_list):
                self.cur_position = 0
                # enemy has reached destination
                # take away hps from player
                ...
