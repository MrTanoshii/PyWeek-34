import arcade

import src.const as C


class Tower(arcade.Sprite):
    """
    Base tower class

    Parameters
    ----------
    name: str
        file name
    label: str
        end user sees this on their screen.
    cost: int
        gold cost of the tower
    level: int
        level of tower, increases damage.
    attack_cooldown_sec: float
        how much it takes to shoot again after shooting in seconds.
    radius: float
        how far can the tower reach, for shooting and recognizing enemies.
    radius_splash: float
        area where splash damage is applied.
    damage_air: float
        damage per bullet for air type enemies, zero if no ground damage.
    damage_ground: float
        damage per bullet for ground type enemies, zero if no ground damage.
    damage_splash: float
        splash damage, zero if no splash damage.
    damage_poison: float
        poison damage, zero if no splash damage.
    """

    # TODO: researches

    def __init__(self, tower_type: dict) -> None:
        super().__init__()
        self.name: str = tower_type["name"]
        self.label: str = tower_type["label"]
        print(C.TOWERS.BASEPATH / tower_type["name"])
        self.texture = arcade.load_texture(C.TOWERS.BASEPATH / tower_type["name"])
        self.level: int = tower_type["level"]

        self.gold_cost: int = tower_type["gold_cost"]
        self.research_cost: int = tower_type["research_cost"]

        self.attack_cooldown_sec: float = tower_type["attack_cooldown_sec"]
        self.cooldown: float = 0
        self.radius: float = tower_type["radius"]
        self.radius_splash: float = tower_type["radius_splash"]

        self.damage_air: float = tower_type["damage_air"]
        self.damage_ground: float = tower_type["damage_ground"]
        self.damage_splash: float = tower_type["damage_splash"]
        self.damage_poison: float = tower_type["damage_poison"]

        self.width: float = C.GRID.WIDTH * tower_type["size_tiles"]
        self.height: float = C.GRID.HEIGHT * tower_type["size_tiles"]
        self.scale: float = C.SETTINGS.GLOBAL_SCALE

        self.size_tiles: int = tower_type["size_tiles"]
