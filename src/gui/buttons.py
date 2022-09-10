import arcade.gui

from typing import Optional, Callable

from arcade.gui import UIEvent, UIMouseMovementEvent, UIMousePressEvent


from src.audio import Audio
from src.towers import TowerHandler
from src import const as C
from .window import Window, Menu


class SwitchButton(arcade.gui.UITextureButton):
    _enabled_texture: arcade.Texture
    _disabled_texture: arcade.Texture
    _default = False

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **{
                "texture": self._enabled_texture
                if self._default
                else self._disabled_texture,
                **kwargs,
            }
        )
        self.enabled = self._default

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        self.enabled = not self.enabled
        self.on_switch()
        if self.enabled:
            self.texture = self._enabled_texture
        else:
            self.texture = self._disabled_texture

    def on_switch(self):
        pass


class SoundButton(SwitchButton):
    _enabled_texture = arcade.load_texture(
        ":resources:onscreen_controls/flat_dark/sound_on.png"
    )
    _disabled_texture = arcade.load_texture(
        ":resources:onscreen_controls/flat_dark/sound_off.png"
    )
    _default = True

    def on_switch(self):
        if self.enabled:
            Audio.unmute()
        else:
            Audio.mute()

    def sync_to_audio_state(self):
        """Keep state synced to audio state.
        Called on every frame.
        """

        # Sync button state to Audio mute state
        if Audio.is_muted:
            self.enabled = False
            self.texture = self._disabled_texture
        else:
            self.enabled = True
            self.texture = self._enabled_texture


class MenuButton(SwitchButton):
    _enabled_texture = arcade.load_texture(
        ":resources:onscreen_controls/flat_dark/close.png"
    )
    _disabled_texture = arcade.load_texture(
        ":resources:onscreen_controls/flat_dark/hamburger.png"
    )

    def __init__(self, *args, **kwargs):
        self.manager: arcade.gui.UIManager = kwargs.pop("manager")
        self.menu: Optional[Menu] = None
        self.restart_func: Callable[[], None] = kwargs.pop("restart_func", None)
        self.toggle_pause_func: Callable[[], None] = kwargs.pop(
            "toggle_pause_func", None
        )
        super().__init__(*args, **kwargs)

    def on_switch(self):
        if self.enabled:
            self.menu = Menu.create(self.restart_func, self.toggle_pause_func)
            self.manager.add(self.menu.center_on_screen())
        elif self.menu:
            self.menu.close()
            self.manager.remove(self.menu)


class TowerButton(arcade.gui.UITextureButton):
    def __init__(self, *args, **kwargs):
        self.tower = kwargs.pop("tower", None)
        self.tower_handler: Optional[TowerHandler] = kwargs.pop("tower_handler", None)

        super().__init__(
            *args,
            **{
                **kwargs,
                "width": C.GUI.TOWER_SIZE,
                "height": C.GUI.TOWER_SIZE,
                "texture": self.tower
                and arcade.load_texture(C.TOWERS.BASEPATH / self.tower["name"]),
            }
        )

    def on_event(self, event: UIEvent):
        # If Hovered
        if isinstance(event, UIMouseMovementEvent):
            self.hovered = self.rect.collide_with_point(event.x, event.y)
        # If Pressed
        if isinstance(event, UIMousePressEvent):
            self.pressed = self.rect.collide_with_point(event.x, event.y)


class RemoveButton(arcade.gui.UITextureButton):
    def __init__(self, *args, **kwargs):
        self.tower_handler: Optional[TowerHandler] = kwargs.pop("tower_handler", None)
        super().__init__(
            *args,
            **{
                **kwargs,
                "texture": arcade.load_texture(
                    ":resources:onscreen_controls/flat_dark/r.png"
                ),
            }
        )

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        if self.tower_handler:
            self.tower_handler.select_tower_type(C.TOWERS.REMOVE_TOWER)
