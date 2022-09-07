import arcade
from .enemy import Enemy
from src import const as C


class EnemyHandler:
    def __init__(self):
        self.enemy_list = arcade.SpriteList()
        position_list = [
            [[780, 0],
             [780, 360],
             [450, 360],
             [450, 440],
             [0, 440],
             [0, 0]],
            [[1280, 440],
             [1080, 440],
             [1080, 400],
             [980, 400],
             [980, 440],
             [0, 440],
             [0, 0],
             [1280, 0]],
            [[980, 720],
             [980, 520],
             [620, 520],
             [620, 440],
             [0, 440],
             [0, 0],
             [1280, 0],
             [1280, 720]],
        ]

        for spd in range(100):
            enemy = Enemy(
                position_list[spd % 3], C.RESOURCES / "enemies" / f"alien{spd % 10}.png", speed=spd / 20, scale=.4
            )
            enemy.center_x = position_list[spd % 3][0][0]
            enemy.center_y = position_list[spd % 3][0][1]
            self.enemy_list.append(enemy)

    def on_draw(self):
        self.enemy_list.draw()

    def on_update(self, delta_time: float):
        self.enemy_list.update()
