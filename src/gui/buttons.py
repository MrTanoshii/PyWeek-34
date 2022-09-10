import arcade.gui
from typing import Optional
from src.audio import Audio
from src.towers import TowerHandler
from src import const as C
from .window import Menu


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
            C.AUDIO.VOLUME["MASTER"] = 1.0
            Audio.play_random(["bgm_1", "bgm_2"])
        else:
            C.AUDIO.VOLUME["MASTER"] = 0
            for sound in Audio.sound_list:  # I guess Audio should be changed
                if "stream_player" in Audio.sound_list[sound]:
                    Audio.stop(sound)


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

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        if self.tower_handler and self.tower:
            self.tower_handler.select_tower_type(self.tower)


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


class MenuButton(SwitchButton):
    _enabled_texture = arcade.load_texture(
        ":resources:onscreen_controls/flat_dark/close.png"
    )
    _disabled_texture = arcade.load_texture(
        ":resources:onscreen_controls/flat_dark/hamburger.png"
    )

    def __init__(self, *args, **kwargs):
        self.manager: Optional[arcade.gui.UIManager] = kwargs.pop("manager", None)
        self.menu: Optional[arcade.gui.UIWidget] = None
        super().__init__(*args, **kwargs)

    def on_switch(self):
        if not self.manager:
            raise ValueError("UIManger is required to open the menu")

        if self.enabled:
            self.menu = Menu.create()
            self.manager.add(self.menu)
        elif self.menu:
            self.manager.remove(self.menu)
