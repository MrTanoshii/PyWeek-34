import arcade.gui
from arcade.gui import UIEvent, UIMouseMovementEvent, UIMousePressEvent
from typing import Optional

from arcade.gui import UIEvent, UIMouseMovementEvent, UIMousePressEvent

from src.audio import Audio
from src.towers import TowerHandler
from src import const as C


class SoundButton(arcade.gui.UITextureButton):
    _enabled_texture = arcade.load_texture(
        ":resources:onscreen_controls/flat_dark/sound_on.png"
    )
    _disabled_texture = arcade.load_texture(
        ":resources:onscreen_controls/flat_dark/sound_off.png"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **{
                "texture": self._enabled_texture,
                **kwargs,
            }
        )
        self.enabled = True

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        self.enabled = not self.enabled
        if self.enabled:
            self.texture = self._enabled_texture
            C.AUDIO.VOLUME["MASTER"] = 1.0
            Audio.play_random(["bgm_1", "bgm_2"])
        else:
            self.texture = self._disabled_texture
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
