from pathlib import Path


class MENU:
    PREVIEW_BASEPATH = Path("src") / "gui" / "sprites"
    LEVELS = {
        # name of map and its preview (e.g. draft_level_1.json and draft_level_1.png)
        "Duck level": "draft_level_secret_duck",
        "Penguin level": "draft_level_secret_penguin",
        "Turtle level": "draft_level_secret_turtle",
        "level 1": "draft_level_1",
        "level 2": "draft_level_2",
        "level 3": "draft_level_3",
        "level 4": "draft_level_4",
        "level 5": "draft_level_5",
    }
    # SECRET_LEVELS = [
    #     "draft_level_secret_duck",
    #     "draft_level_secret_penguin",
    #     "draft_level_secret_turtle",
    # ]
    SECRET_LEVELS = []
    LEVELS_IN_ROW = 3
    HOVER_COLOR = (0, 0, 0, 48)
