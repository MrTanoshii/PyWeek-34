class AUDIO:
    BASE_PATH = "src/audio/resources/"
    VOLUME = {"MASTER": 1.0, "BGM": 1.0, "SFX": 1.0}

    MASTER_LIST = {
        "bgm_1": {
            "path": "460357__doctor-dreamchip__circuit-synthwave_trimmed.wav",
            "gain": -0.7,
            "loop": True,
            "multiple": False,
            "type": "BGM",
        },
        "bgm_2": {
            "path": "615546__projecteur__cosmic-dark-synthwave.mp3",
            "gain": -0.7,
            "loop": True,
            "multiple": False,
            "type": "BGM",
        },
        "gulag_alarm": {
            "path": "400894__bowlingballout__honk-alarm-repeat-loop.mp3",
            "gain": -0.7,
            "loop": False,
            "multiple": False,
            "type": "SFX",
        },
        "tower_cannon_shoot": {
            "path": "440147__dpren__scifi-gun-mega-charge-cannon_trimmed.wav",
            "gain": -0.7,
            "loop": False,
            "multiple": False,
            "type": "SFX",
        },
    }
