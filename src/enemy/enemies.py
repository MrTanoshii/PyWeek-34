bottle_of_liquid = {
    "hp": 20,
    "speed": 200,
    "flying": False,
    "boss": False,
    "gold_drop": 3,
    "image": "alien7.png",
    "scale": 0.3,
    "wobble": [7, 6],
}
martian_snake = {
    "hp": 60,
    "speed": 110,
    "flying": False,
    "boss": False,
    "gold_drop": 9,
    "image": "alien3.png",
    "scale": 0.3,
    "wobble": [5, 3],
}
martian_dog = {
    "hp": 95,
    "speed": 150,
    "flying": False,
    "boss": False,
    "gold_drop": 15,
    "image": "alien6.png",
    "scale": 0.3,
    "wobble": [4, 4],
}
martian_unicorn = {
    "hp": 120,
    "speed": 130,
    "flying": False,
    "boss": False,
    "gold_drop": 18,
    "image": "alien2.png",
    "scale": 0.4,
    "wobble": [3, 3],
}
martian_wolf = {
    "hp": 250,
    "speed": 80,
    "flying": False,
    "boss": False,
    "gold_drop": 30,
    "image": "alien0.png",
    "scale": 0.4,
    "wobble": [2, 4],
}
martian_fireman = {
    "hp": 2500,
    "speed": 50,
    "flying": False,
    "boss": True,
    "gold_drop": 150,
    "image": "alien5.png",
    "scale": 0.6,
    "wobble": [3, 2],
}
martian_bart = {
    "hp": 300,
    "speed": 77,
    "flying": False,
    "boss": False,
    "gold_drop": 30,
    "image": "alien4.png",
    "scale": 0.4,
    "wobble": [1, 3],
}
martian_grinch = {
    "hp": 500,
    "speed": 95,
    "flying": False,
    "boss": False,
    "gold_drop": 30,
    "image": "alien1.png",
    "scale": 0.4,
    "wobble": [2, 1],
}
bear = {
    "hp": 800,
    "speed": 70,
    "flying": False,
    "boss": False,
    "gold_drop": 35,
    "image": "alien8.png",
    "scale": 0.4,
    "wobble": [3, 3],
}
drunken_bear = {
    "hp": 15000,
    "speed": 69,
    "flying": False,
    "boss": True,
    "gold_drop": 2500,
    "image": "alien9.png",
    "scale": 0.5,
    "wobble": [3, 3],
}


mech_duck = [
    {
        "hp": 123 * (duck + 1),
        "speed": 90 + (duck * 5),
        "flying": False,
        "boss": False,
        "gold_drop": ((duck + 5) * 5),
        "image": f"mech_duck_{duck}.png",
        "scale": 0.3,
        "wobble": [4, 4],
    }
    for duck in range(15)
]

enemies = [
    bottle_of_liquid,
    martian_snake,
    martian_dog,
    martian_unicorn,
    martian_wolf,
    martian_fireman,
    martian_bart,
    martian_grinch,
    bear,
    drunken_bear,
]
# enemies = [infantry, heavy_infantry, scout, tank, plane]
