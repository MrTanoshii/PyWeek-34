import arcade
import arcade.gui

from resources import Gold
from src import const as C
from src.towers.tower_handler import TowerHandler
from .buttons import *
from .popup import Popup


class GUI:
    def __init__(
        self,
        tower_handler: TowerHandler,
        notification_handler,
        restart_func,
        back_to_menu_func,
    ):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.is_paused = False

        self.tower_handler = tower_handler

        self.restart_func = restart_func  # perkele
        self.back_to_menu_func = back_to_menu_func
        # i don't like it, but we need info about current level to restart it
        # (interfaces, di and non god-object map class would help here)

        self.notification_handler = notification_handler

        self.h_box = arcade.gui.UIBoxLayout(vertical=False)
        self.button_box = None
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

        self.sound_button = SoundButton()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                child=self.sound_button.with_space_around(
                    C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING, C.GUI.PADDING
                ),
            )
        )

        self.menu_button = MenuButton(
            manager=self.manager,
            restart_func=self.restart_func,
            toggle_pause_func=self.toggle_pause,
            back_to_menu_func=self.back_to_menu_func,
        )  # ei mukavaa

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="top",
                child=self.menu_button.with_space_around(
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
        # print(Gold.get())

    def draw_button_box(self, center_x, center_y, width, height):
        """draws the shaded background for button tooltips"""
        arcade.draw_rectangle_filled(
            center_x=center_x,
            center_y=center_y,
            width=width,
            height=height,
            color=(0, 0, 0, 128),
        )

    def on_update(self):
        self.button_box = None
        # hover and selected logic
        for button in self.tower_buttons:
            if button.pressed:
                self.tower_handler.selected_type = button.tower
            elif button.hovered:
                offset = 100
                ttl = 0.3  # time to live for these stats

                # It should have been created with UILabel, not Notification

                self.notification_handler.create(
                    text=button.tower["label"],
                    x=button.center_x - button.width / 2,
                    y=button.center_y + button.height + offset,
                    color=arcade.color.BLANCHED_ALMOND,
                    ttl=ttl,
                )
                offset -= 20
                self.notification_handler.create(
                    text=f"Cost: {button.tower['gold_cost']}",
                    x=button.center_x - button.width / 2,
                    y=button.center_y + button.height + offset,
                    color=arcade.color.BLANCHED_ALMOND,
                    ttl=ttl,
                )
                offset -= 20
                if button.tower["radius"] != 0:
                    self.notification_handler.create(
                        text=f"Range: {button.tower['radius']}",
                        x=button.center_x - button.width / 2,
                        y=button.center_y + button.height + offset,
                        color=arcade.color.BLANCHED_ALMOND,
                        ttl=ttl,
                    )
                    offset -= 20
                if button.tower["damage_ground"] != 0:
                    self.notification_handler.create(
                        text=f"Damage: {button.tower['damage_ground']}",
                        x=button.center_x - button.width / 2,
                        y=button.center_y + button.height + offset,
                        color=arcade.color.BLANCHED_ALMOND,
                        ttl=ttl,
                    )
                    offset -= 20
                if button.tower["radius"] != 0:
                    self.notification_handler.create(
                        text=f"Cooldown: {button.tower['attack_cooldown_sec']} s",
                        x=button.center_x - button.width / 2,
                        y=button.center_y + button.height + offset,
                        color=arcade.color.BLANCHED_ALMOND,
                        ttl=ttl,
                    )
                    offset -= 20
                if button.tower["damage_poison"]:
                    self.notification_handler.create(
                        text=f"Poison Damage: {button.tower['damage_poison']} /s",
                        x=button.center_x - button.width / 2,
                        y=button.center_y + button.height + offset,
                        color=arcade.color.BLANCHED_ALMOND,
                        ttl=ttl,
                    )
                    offset -= 20
                if button.tower.get("slow", False):
                    self.notification_handler.create(
                        text=f"Slows Enemies",
                        x=button.center_x - button.width / 2,
                        y=button.center_y + button.height + offset,
                        color=arcade.color.BLANCHED_ALMOND,
                        ttl=ttl,
                    )
                    offset -= 20
                if button.tower.get("label", 0) == "Base tower":
                    self.notification_handler.create(
                        text=f"Necessary foundation",
                        x=button.center_x - button.width / 2,
                        y=button.center_y + button.height + offset,
                        color=arcade.color.BLANCHED_ALMOND,
                        ttl=ttl,
                    )
                    offset -= 20
                    self.notification_handler.create(
                        text=f"for all towers.",
                        x=button.center_x - button.width / 2,
                        y=button.center_y + button.height + offset,
                        color=arcade.color.BLANCHED_ALMOND,
                        ttl=ttl,
                    )
                    offset -= 30
                    self.notification_handler.create(
                        text=f"Safety First!",
                        x=button.center_x - button.width / 2,
                        y=button.center_y + button.height + offset,
                        color=arcade.color.BLANCHED_ALMOND,
                        ttl=ttl,
                    )
                    offset -= 20
                self.button_box = (
                    button.center_x + 60,
                    button.center_y + 120,
                    200,
                    140,
                )

        if self.sound_button is not None:
            self.sound_button.sync_to_audio_state()

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

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def on_died(self):
        self.manager.add(
            Popup.create("You died", self.restart_func, self.back_to_menu_func)
        )

    def on_win(self):
        self.manager.add(
            Popup.create("You win", self.restart_func, self.back_to_menu_func)
        )
