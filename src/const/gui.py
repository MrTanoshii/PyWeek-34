from pathlib import Path


class GUI:
    TOWER_SIZE = 64
    PADDING = 20
    RESOURCE_FONT_SIZE = 18
    GOLD_COLOR = (255, 215, 0, 255)
    LIVES_COLOR = (200, 200, 200, 255)
    SCORE_COLOR = (128, 128, 255, 255)
    TOWER_SELECT_COLOR = (255, 255, 255, 255)
    BUTTONS_GAP = 20
    MENU_BG = Path("src") / "towers" / "sprites" / "mg2.png"  # TODO: change this
    POPUP_TEXT_COLOR = (21, 19, 21)  # from arcade flat buttons
