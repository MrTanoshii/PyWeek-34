import arcade
import arcade.gui

from src import const as C
from src.towers.tower_handler import TowerHandler
from .buttons import *


class GUI:
    def __init__(self, tower_handler: TowerHandler, notification_handler):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.tower_handler = tower_handler
        self.notification_handler = notification_handler

        self.h_box = arcade.gui.UIBoxLayout(vertical=False)

        self.tower_buttons = []

        # Check if tower type is selected, and it is not base tower
        for tower in C.TOWERS.ALL_TOWERS:
            self.tower_buttons.append(
                TowerButton(tower=tower, tower_handler=tower_handler)
            )

        for button in self.tower_buttons:
            self.h_box.add(button.with_space_around(C.GUI.PADDING, C.GUI.PADDING, 0, 0))

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

    def draw_tower_selection(self):
        for button in self.tower_buttons:
            if self.tower_handler.selected_type == button.tower and button.hovered:
                arcade.draw_rectangle_filled(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    (0, 255, 0, 16),
                )
            elif self.tower_handler.selected_type == button.tower:
                arcade.draw_rectangle_filled(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    (0, 255, 0, 32),
                )
            elif button.hovered:
                arcade.draw_rectangle_filled(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    (255, 255, 255, 32),
                )
            else:
                arcade.draw_rectangle_filled(
                    button.center_x,
                    button.center_y,
                    button.width + C.GUI.PADDING,
                    button.height + C.GUI.PADDING,
                    (255, 255, 255, 16),
                )

    def on_update(self):
        # hover and selected logic
        for button in self.tower_buttons:
            if button.pressed:
                self.tower_handler.selected_type = button.tower
            elif button.hovered:

                self.notification_handler.create(
                    text=button.tower["label"],
                    x=button.center_x - button.width / 2,
                    y=button.center_y + button.height,
                    color=arcade.color.BLANCHED_ALMOND,
                )

    def on_key_press(self, symbol, _modifiers):
        for i in range(len(self.tower_buttons)):
            if symbol == i + 49:  # number "1" is symbol 49
                self.tower_handler.selected_type = self.tower_buttons[i + 1].tower
        # Deselect tower and tower type
        if (
            symbol == arcade.key.ASCIITILDE
            or symbol == arcade.key.B
            or symbol == 944892805120
            or symbol == 824633720832
            or symbol == 96
        ):
            self.tower_handler.selected_type = self.tower_buttons[0].tower

        if symbol == arcade.key.ESCAPE:
            self.tower_handler.selected_type = C.TOWERS.BASE_TOWER
            self.tower_handler.selected_tower = None
