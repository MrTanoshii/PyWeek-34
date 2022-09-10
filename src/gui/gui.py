import arcade
import arcade.gui

from src import const as C
from .buttons import *


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
                button.with_space_around(C.GUI.PADDING, C.GUI.PADDING, 0, C.GUI.PADDING)
            )

        # Create a widget to hold the h_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="bottom", child=self.h_box, align_y=+6
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
            if self.tower_handler.selected_type == button.tower and button.hovered:
                arcade.draw_rectangle_filled(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    (255, 0, 0, 32),
                )
            elif self.tower_handler.selected_type == button.tower:
                arcade.draw_rectangle_filled(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    (255, 0, 0, 64),
                )
            elif button.hovered:
                arcade.draw_rectangle_filled(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    (255, 255, 255, 64),
                )
            else:
                arcade.draw_rectangle_filled(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    (255, 255, 255, 32),
                )

    def on_update(self):
        for button in self.tower_buttons:
            if button.pressed:
                self.tower_handler.selected_type = button.tower

    def on_key_press(self, symbol, _modifiers):
        for i in range(len(self.tower_buttons)):
            if symbol == i + 49:  # number "1" is symbol 49
                self.tower_handler.selected_type = self.tower_buttons[i].tower
