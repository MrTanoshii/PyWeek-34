from src.enemy.enemies import enemies as e


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
        return [enemies, len(enemies)// 3]
