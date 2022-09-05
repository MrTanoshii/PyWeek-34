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
    level: int
        level of tower, increases damage.
    attack_cooldown_ms: float
        how much it takes to shoot again after shooting in milliseconds.
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

    def __init__(
        self,
        name: str = "",
        label: str = "",
        level: int = 0,
        attack_cooldown_ms: float = 0,
        radius: float = 0,
        radius_splash: float = 0,
        damage_air: float = 0,
        damage_ground: float = 0,
        damage_splash: float = 0,
        damage_poison: float = 0,
    ) -> None:
        super().__init__()
        self.name: str = name
        self.label: str = label

        self.level: int = level

        self.attack_cooldown_ms: float = attack_cooldown_ms
        self.radius: float = radius
        self.radius_splash: float = radius_splash

        self.damage_air: float = damage_air
        self.damage_ground: float = damage_ground
        self.damage_splash: float = damage_splash
        self.damage_poison: float = damage_poison

        self.texture = arcade.load_texture(C.RESOURCES / "towers" / self.name)
