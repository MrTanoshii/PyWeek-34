import arcade
import arcade.gui

from src import const as C
from towers.tower_handler import TowerHandler
from .buttons import *


class GUI:
    def __init__(self, tower_handler: TowerHandler, notification_handler):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.tower_handler = tower_handler
        self.notification_handler = notification_handler

        self.h_box = arcade.gui.UIBoxLayout(vertical=False)

        self.tower_buttons = []
        # check if they changed, if they did write into tower_buttons
        self.temporary_tower_buttons = []

        # Check if tower type is selected, and it is not base tower
        self.tower_buttons.append(
            TowerButton(tower=C.TOWERS.BASE_TOWER, tower_handler=tower_handler)
        )

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

    def draw_tower_selection(self):
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
        # hover and selected logic
        for button in self.tower_buttons:
            if button.pressed:
                self.tower_handler.selected_type = button.tower
            elif button.hovered:

                self.notification_handler.create(
                    text=button.tower["label"],
                    x=button.center_x,
                    y=button.center_y + button.height,
                    color=arcade.color.BLANCHED_ALMOND,
                )

        # Select tower selection options

        self.h_box.clear()
        self.temporary_tower_buttons.clear()

        # Tower selected
        if self.tower_handler.selected_tower:
            # only base tower -> 3 types (lvl 1)
            if self.tower_handler.selected_tower.name == C.TOWERS.BASE_TOWER["name"]:
                self.temporary_tower_buttons.append(
                    TowerButton(
                        tower=C.TOWERS.CANNON_TOWER,
                        tower_handler=self.tower_handler,
                    )
                )
                self.temporary_tower_buttons.append(
                    TowerButton(
                        tower=C.TOWERS.MG_TOWER, tower_handler=self.tower_handler
                    )
                )
                self.temporary_tower_buttons.append(
                    TowerButton(
                        tower=C.TOWERS.MISSILE, tower_handler=self.tower_handler
                    )
                )
            # only cannon tower -> show cannon options
            elif self.tower_handler.selected_tower.name in [
                C.TOWERS.CANNON_TOWER["name"],
                C.TOWERS.CANNON2_TOWER["name"],
                C.TOWERS.CANNON3_TOWER["name"],
            ]:
                self.add_tower_options(
                    [
                        C.TOWERS.CANNON_TOWER,
                        C.TOWERS.CANNON2_TOWER,
                        C.TOWERS.CANNON3_TOWER,
                    ]
                )
            # only MG tower -> show cannon options
            elif self.tower_handler.selected_tower.name in [
                C.TOWERS.MG_TOWER["name"],
                C.TOWERS.MG_TOWER2["name"],
                C.TOWERS.MG_TOWER3["name"],
            ]:
                self.add_tower_options(
                    [C.TOWERS.MG_TOWER, C.TOWERS.MG_TOWER2, C.TOWERS.MG_TOWER3]
                )
            # only MG tower -> show cannon options
            elif self.tower_handler.selected_tower.name in [
                C.TOWERS.MISSILE["name"],
                C.TOWERS.MISSILE2["name"],
                C.TOWERS.MISSILE3["name"],
            ]:
                self.add_tower_options(
                    [C.TOWERS.MISSILE, C.TOWERS.MISSILE2, C.TOWERS.MISSILE3]
                )

        # No Tower selected
        else:
            # no selection -> base tower
            self.temporary_tower_buttons.append(
                TowerButton(tower=C.TOWERS.BASE_TOWER, tower_handler=self.tower_handler)
            )
            self.tower_handler.selected_type = C.TOWERS.BASE_TOWER

        for i in range(len(self.temporary_tower_buttons)):
            if self.temporary_tower_buttons[i].tower != self.tower_buttons[i].tower:
                if C.DEBUG.ALL:
                    print("Tower selection list updated")
                self.tower_buttons.clear()
                self.tower_buttons = self.temporary_tower_buttons
                break

        for button in self.tower_buttons:
            self.h_box.add(
                button.with_space_around(C.GUI.PADDING, C.GUI.PADDING, 0, C.GUI.PADDING)
            )

    def add_tower_options(self, options):
        for option in options:
            self.tower_buttons.append(
                TowerButton(
                    tower=option,
                    tower_handler=self.tower_handler,
                )
            )

    def on_key_press(self, symbol, _modifiers):
        for i in range(len(self.tower_buttons)):
            if symbol == i + 49:  # number "1" is symbol 49
                self.tower_handler.selected_type = self.tower_buttons[i].tower
        # Deselect tower and tower type
        if symbol == arcade.key.ESCAPE:
            self.tower_handler.selected_type = C.TOWERS.BASE_TOWER
            self.tower_handler.selected_tower = None
