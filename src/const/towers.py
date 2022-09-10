from pathlib import Path

from src.towers import *


class TOWERS:
    BASEPATH = Path("src/towers/sprites")
    RADIUS_BG_COLOR = (255, 255, 255, 64)
    SELECTED_OUTLINE_COLOR = (255, 255, 255, 255)

    REMOVE_TOWER = {
        "remove": True,
    }  # хуета какая-то на самом деле, но ладно -_-

    # Different tower types
    BASE_TOWER = {
        "name": "Tower.png",
        "label": "Base tower",
        "level": 0,
        "attack_cooldown_sec": 1,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 5,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 0,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    CANNON_TOWER = {
        "name": "Cannon.png",
        "label": "Cannon I",
        "level": 0,
        "attack_cooldown_sec": 1,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 5,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 3,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    CANNON2_TOWER = {
        "name": "Cannon2.png",
        "label": "Cannon II",
        "level": 0,
        "attack_cooldown_sec": 1,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 5,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 3,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    CANNON3_TOWER = {
        "name": "Cannon3.png",
        "label": "Cannon III",
        "level": 0,
        "attack_cooldown_sec": 1,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 5,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 3,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    MG_TOWER = {
        "name": "mg.png",
        "label": "MG I",
        "level": 0,
        "attack_cooldown_sec": 1,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 5,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 50,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    MG_TOWER2 = {
        "name": "mg2.png",
        "label": "MG II",
        "level": 0,
        "attack_cooldown_sec": 1,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 5,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 50,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    MG_TOWER3 = {
        "name": "mg3.png",
        "label": "MG III",
        "level": 0,
        "attack_cooldown_sec": 0.2,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 3,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 5,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    MISSILE = {
        "name": "Missile_Launcher.png",
        "label": "Rocket Launcher I",
        "level": 0,
        "attack_cooldown_sec": 5,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 14,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 50,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }

    MISSILE2 = {
        "name": "Missile_Launcher2.png",
        "label": "Rocket Launcher II",
        "level": 0,
        "attack_cooldown_sec": 5,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 5,
        "radius_splash": 0,
        "damage_air": 16,
        "damage_ground": 80,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    MISSILE3 = {
        "name": "Missile_Launcher3.png",
        "label": "Rocket Launcher III",
        "level": 0,
        "attack_cooldown_sec": 5,
        "gold_cost": 100,
        "research_cost": 0,
        "radius": 18,
        "radius_splash": 0,
        "damage_air": 0,
        "damage_ground": 100,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
    ALL_TOWERS = [
        CANNON_TOWER,
        CANNON2_TOWER,
        CANNON3_TOWER,
        MG_TOWER,
        MG_TOWER2,
        MG_TOWER3,
        MISSILE,
        MISSILE2,
        MISSILE3,
    ]
