from src.enemy.enemies import enemies as e
from src.enemy.enemies import mech_duck as m


def add_mech_duck(
    _0: int = 0,
    _1: int = 0,
    _2: int = 0,
    _3: int = 0,
    _4: int = 0,
    _5: int = 0,
    _6: int = 0,
    _7: int = 0,
    _8: int = 0,
    _9: int = 0,
    _10: int = 0,
    _11: int = 0,
    _12: int = 0,
    _13: int = 0,
    _14: int = 0,
):
    wave = []
    wave = wave + [m[0]] * _0
    wave = wave + [m[1]] * _1
    wave = wave + [m[2]] * _2
    wave = wave + [m[3]] * _3
    wave = wave + [m[4]] * _4
    wave = wave + [m[5]] * _5
    wave = wave + [m[6]] * _6
    wave = wave + [m[7]] * _7
    wave = wave + [m[8]] * _8
    wave = wave + [m[9]] * _9
    wave = wave + [m[10]] * _10
    wave = wave + [m[11]] * _11
    wave = wave + [m[12]] * _12
    wave = wave + [m[13]] * _13
    wave = wave + [m[14]] * _14

    return wave


def add_enemy(
    _0: int = 0,
    _1: int = 0,
    _2: int = 0,
    _3: int = 0,
    _4: int = 0,
    _5: int = 0,
    _6: int = 0,
    _7: int = 0,
    _8: int = 0,
    _9: int = 0,
):
    wave = []
    wave = wave + [e[0]] * _0
    wave = wave + [e[1]] * _1
    wave = wave + [e[2]] * _2
    wave = wave + [e[3]] * _3
    wave = wave + [e[4]] * _4
    wave = wave + [e[5]] * _5
    wave = wave + [e[6]] * _6
    wave = wave + [e[7]] * _7
    wave = wave + [e[8]] * _8
    wave = wave + [e[9]] * _9

    return wave


class Waves:
    @staticmethod
    def wave_1_1():
        return [[e[6]] * 24 + [e[0]], 14]

    @staticmethod
    def wave_1_2():
        return [
            [
                e[5],
                e[6],
                e[1],
                e[2],
                e[4],
            ],
            7,
        ]

    @staticmethod
    def wave_1_3():
        enemies = []
        enemies = enemies + [e[2]] * 50
        enemies = enemies + [e[5]] * 30
        enemies = enemies + [e[7]] * 30
        return [enemies, len(enemies) // 3]

    @classmethod
    def level_1(cls, wave: int):

        if wave == 1:
            _wave = add_enemy(20, 25, 22, 5, 1, 0, 0, 0, 0, 0)
        elif wave == 2:
            _wave = add_enemy(20, 25, 22, 20, 5, 1, 0, 0, 0, 0)
        elif wave == 3:
            _wave = add_enemy(20, 25, 22, 25, 22, 5, 1, 0, 0, 0)
        elif wave == 4:
            _wave = add_enemy(20, 25, 22, 22, 450, 20, 5, 1, 0, 0)
        elif wave == 5:
            _wave = add_enemy(20, 25, 22, 45, 0, 20, 120, 5, 1, 0)
        elif wave == 6:
            _wave = add_enemy(20, 25, 22, 450, 44, 20, 13, 8, 5, 1)
        elif wave == 7:
            _wave = add_enemy(20, 25, 22, 45, 0, 20, 55, 74, 12, 5)
        elif wave == 8:
            _wave = add_enemy(20, 25, 22, 45, 11, 20, 68, 78, 123, 25)
        elif wave == 9:
            _wave = add_enemy(20, 25, 22, 45, 12, 20, 14, 159, 753, 100)
        else:
            return None
        return [_wave, len(_wave) // wave]

    @classmethod
    def level(cls, map: str, wave: int):
        print(map)
        if map == "draft_level_secret_duck.json":
            return cls.level_duck(wave)
        else:
            return cls.level_1(wave)

    @classmethod
    def level_duck(cls, wave: int):
        if wave == 1:
            ducks = add_mech_duck(20, 25, 22, 45)
        elif wave == 2:
            ducks = add_mech_duck(0, 0, 0, 20, 25, 22, 45)
        elif wave == 3:
            ducks = add_mech_duck(0, 0, 0, 0, 0, 0, 0, 0, 20, 25, 22, 45)
        elif wave == 4:
            ducks = add_mech_duck(0, 0, 0, 0, 20, 25, 22, 450, 0, 0, 0, 0, 12)
        elif wave == 5:
            ducks = add_mech_duck(20, 25, 22, 45, 0, 0, 0, 120, 100, 75, 22)
        elif wave == 6:
            ducks = add_mech_duck(20, 25, 22, 45, 0, 0, 0, 0, 0, 44, 22, 13, 8, 7, 2)
        elif wave == 7:
            ducks = add_mech_duck(20, 25, 22, 45, 0, 41, 55, 74, 12, 13, 5)
        elif wave == 8:
            ducks = add_mech_duck(20, 25, 22, 45, 11, 45, 68, 78, 123)
        elif wave == 9:
            ducks = add_mech_duck(20, 25, 22, 45, 12, 123, 14, 159, 753, 656)
        else:
            return None
        return [ducks, len(ducks) // wave]
