import arcade
from .enemy import Enemy
from src import const as C


class EnemyHandler:
    def __init__(self):
        self.enemy_list = arcade.SpriteList()
        position_list = [
            [50, 50],
            [900, 25],
            [1100, 250],
            [50, 250],
            [200, 400],
            [1200, 650],
            [50, 700],
        ]

        for spd in range(10):
            enemy = Enemy(
                position_list, C.RESOURCES / "enemies" / "alien1.png", speed=spd
            )
            enemy.center_x = position_list[0][0]
            enemy.center_y = position_list[0][1]
            self.enemy_list.append(enemy)

    def on_draw(self):
        self.enemy_list.draw()

    def on_update(self, delta_time: float):
        self.enemy_list.update()
