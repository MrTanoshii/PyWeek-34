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

        self.tower_buttons = [
            TowerButton(tower=tower, tower_handler=tower_handler)
            for tower in C.TOWERS.ALL_TOWERS
        ]
        for button in self.tower_buttons:
            self.h_box.add(
                button.with_space_around(
                    C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING
                )
            )

        # Create a widget to hold the h_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.h_box, align_y=-300
            )
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=RemoveButton(tower_handler=self.tower_handler).with_space_around(
                    C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING
                ),
                anchor_x="right",
                anchor_y="bottom",
            )
        )

        sound_button = SoundButton()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                child=sound_button.with_space_around(
                    C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING
                ),
            )
        )

    def draw_tower_selection(self):  # fuck it
        for button in self.tower_buttons:
            if self.tower_handler.selected_type == button.tower:
                arcade.draw_rectangle_outline(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    C.GUI.TOWER_SELECT_COLOR,
                )
