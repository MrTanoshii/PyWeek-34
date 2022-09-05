from classes.tower import Tower


class AntiAirTower(Tower):
    name = "anti-air-1.png"
    label = "Anti air tower"
    attack_cooldown_ms = 1000
    radius = 5
    damage_air = 50
