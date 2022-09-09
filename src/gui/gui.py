import arcade
import arcade.gui

from src import const as C
from .buttons import *  # Fuck it


class GUI:
    def __init__(self, tower_handler: TowerHandler):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.tower_handler = tower_handler

        self.h_box = arcade.gui.UIBoxLayout(vertical=False)

        tower_buttons = [
            TowerButton(tower=tower, tower_handler=tower_handler).with_space_around(
                20, 20, 20, 20
            )
            for tower in C.TOWERS.ALL_TOWERS
        ]
        for button in tower_buttons:
            self.h_box.add(button)

        # Create a widget to hold the h_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.h_box, align_y=-300
            )
        )

        sound_button = SoundButton()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                child=sound_button.with_space_around(20, 20, 20, 20),
            )
        )
