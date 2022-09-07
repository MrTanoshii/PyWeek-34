from src.towers import *


class TOWERS:
    RADIUS_BG_COLOR = (255, 255, 255, 64)
    SELECTED_OUTLINE_COLOR = (255, 255, 255, 255)

    # Different tower types
    BASE_TOWER = {
        "name": "anti-air-1.png",
        "label": "Base tower",
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
    ANTIAIR_TOWER = {
        "name": "anti-air-1.png",
        "label": "Anti air tower",
        "level": 0,
        "attack_cooldown_sec": 1,
        "gold_cost": 200,
        "research_cost": 0,
        "radius": 5,
        "radius_splash": 0,
        "damage_air": 50,
        "damage_ground": 0,
        "damage_splash": 0,
        "damage_poison": 0,
        "size_tiles": 2,
    }
