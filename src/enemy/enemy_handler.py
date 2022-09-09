import arcade
from functools import partial
from operator import itemgetter

import src.const as C
from world import World
from .enemy import Enemy
from src.world import *
from .enemies import enemies


class EnemyHandler:
    def __init__(self, world: World):
        """Constructor.

        Keyword Arguments:
        world: World -- World object
        """

        self.enemy_list = arcade.SpriteList()
        self.world = world
        self.spawners = list(map(partial(Spawner, world), self.world.spawners))

        position_list = self.spawners[
            0
        ].path  # TODO: spawning enemies in multiple spawners, should we?
        self.positions = position_list

        self.wave = []
        self.time_between_spawns = 0
        self.time_to_next_spawn = 0

    def on_draw(self):
        self.enemy_list.draw()

    def on_update(self, delta_time: float):
        for enemy in self.enemy_list:
            enemy.update(delta_time)
        # if any units remain in the spawn list
        if self.wave:
            # advance duration remaining time passed since last update
            self.time_to_next_spawn -= delta_time
            # if no time remains
            if self.time_to_next_spawn < 0:
                self.time_to_next_spawn = self.time_between_spawns
                # pop enemy out of wave list
                current_quota = self.wave[0]
                new_enemy_dict = current_quota[0]
                current_quota[1] -= 1
                if current_quota[1] <= 0:
                    self.wave.pop(0)
                    if not self.wave:
                        pass  # TODO: wave ended message
                # place enemy at first spawn
                new_enemy = Enemy(
                    self.positions,
                    **new_enemy_dict,
                )
                new_enemy.center_x = self.positions[0][0]
                new_enemy.center_y = self.positions[0][1]

                self.enemy_list.append(new_enemy)

    def send_wave(self, wave: list, duration: float):
        self.wave = wave
        self.time_between_spawns = duration / sum(map(itemgetter(1), wave))
        self.time_to_next_spawn = self.time_between_spawns
