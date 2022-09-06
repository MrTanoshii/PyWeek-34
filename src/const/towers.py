from classes.tower import Tower


class BaseTower(Tower):
    name = "anti-air-1.png"
    label = "Base tower"
    attack_cooldown_sec = 1
    cost = 100
    radius = 5
    damage_ground = 50


class AntiAirTower(Tower):
    name = "anti-air-1.png"
    label = "Anti air tower"
    attack_cooldown_sec = 1
    cost = 200
    radius = 5
    damage_air = 50


class TOWERS:
    DEFAULT_TOWER = BaseTower
    START_GOLD = DEFAULT_TOWER.cost
    RADIUS_BG_COLOR = (255, 255, 255, 64)
    SELECTED_OUTLINE_COLOR = (255, 255, 255, 255)
