import arcade
from functools import partial
from operator import itemgetter

import src.const as C
from src.world import World
from .enemy import Enemy
from src.world import *
from .enemies import enemies
from src.gamedata import GameData
from src.resources import Lives


class EnemyHandler:
    def __init__(self, world: World, tiled_name: str):
        """Constructor.

        Keyword Arguments:
        world: World -- World object
        """

        self.enemy_list = arcade.SpriteList()
        self.world = world
        self.tiled_name = tiled_name
        self.spawners = list(map(partial(Spawner, world), self.world.spawners))

        position_list = self.spawners[
            0
        ].path  # TODO: spawning enemies in multiple spawners, should we?
        self.positions = position_list
        self.frames_until_next_wave = 300
        self.current_wave = 0
        self.wave = []
        self.time_between_spawns = 0
        self.time_to_next_spawn = 0

    def on_draw(self):
        self.enemy_list.draw()
        for enemy in self.enemy_list:
            enemy.health_bar.on_draw()

    def on_update(self, delta_time: float):
        for enemy in self.enemy_list:
            enemy.update(delta_time)
        if Lives.get() < 1:
            return
        # if any units remain in the spawn list
        if self.wave:
            # advance duration remaining time passed since last update
            self.time_to_next_spawn -= delta_time
            # if no time remains
            if self.time_to_next_spawn < 0:
                self.time_to_next_spawn = self.time_between_spawns
                # pop enemy out of wave list
                new_enemy_dict = self.wave.pop(0)
                # place enemy at first spawn
                new_enemy = Enemy(
                    self.positions,
                    **new_enemy_dict,
                )
                new_enemy.center_x = self.positions[0][0]
                new_enemy.center_y = self.positions[0][1]

                self.enemy_list.append(new_enemy)
        # if all enemies are dead

        if len(self.enemy_list) == 0:
            # count down some frames
            self.frames_until_next_wave -= 1
            if self.frames_until_next_wave < 0:
                self.frames_until_next_wave = 60
                self.current_wave += 1
                # This will need to not be hardcoded to level 1
                wave = C.Waves.level(self.tiled_name, self.current_wave)
                if wave:
                    self.send_wave(*wave)
                if wave is None:
                    print("end of spawns")
                    World.completed_levels.append(self.world.map_name)
                    GameData.write_data()
        else:
            self.frames_until_next_wave = 60

    def send_wave(self, wave: list, duration: float):
        self.wave = wave
        self.time_between_spawns = duration / len(wave)
        self.time_to_next_spawn = self.time_between_spawns
