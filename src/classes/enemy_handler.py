import arcade
from functools import partial
from .enemy import Enemy
from .world import World
from .spawner import Spawner
from src import const as C


class EnemyHandler:
    def __init__(self, world: World):
        self.enemy_list = arcade.SpriteList()
        self.world = world
        self.spawners = list(map(partial(Spawner, world), self.world.spawners))

        position_list = self.spawners[0].path
        self.positions = position_list

        for spd in range(1, 2):
            enemy = Enemy(
                position_list, C.RESOURCES / "enemies" / "alien1.png", speed=spd * 10
            )
            enemy.center_x = position_list[0][0]
            enemy.center_y = position_list[0][1]
            self.enemy_list.append(enemy)

    def on_draw(self):
        self.enemy_list.draw()

    def on_update(self, delta_time: float):
        self.enemy_list.update()
