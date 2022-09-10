from pathlib import Path


class MENU:
    PREVIEW_BASEPATH = Path("src") / "world" / "previews"
    LEVELS = {
        "level 1 name": "draft_level_1",  # name of map and its preview (e.g. draft_level_1.json and draft_level_1.png)
        "level 2 name": "draft_level_2",
        "level 3 name": "draft_level_1",
        "level 4 name": "draft_level_1",
        "level 5 name": "draft_level_1",
        "level 6 name": "draft_level_1",
        "level 7 name": "draft_level_1",
        "level 8 name": "draft_level_1",
    }  # TODO
    SECRET_LEVELS = ["draft_level_3"]  # TODO
    LEVELS_IN_ROW = 3
    HOVER_COLOR = (0, 0, 0, 48)
