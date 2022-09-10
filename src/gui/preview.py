import arcade.gui

import src.const as C


class Preview(arcade.gui.UITextureButton):
    def __init__(self, *args, **kwargs):
        self.map_name = kwargs.pop("map_name")
        self.label = kwargs.pop("label")
        hovered = arcade.load_texture(
            C.MENU.PREVIEW_BASEPATH / f"{self.map_name}.png",
        )
        hovered = hovered.create_filled(
            "hovered_preview", (hovered.width, hovered.height), C.MENU.HOVER_COLOR
        )
        super().__init__(
            *args,
            **{
                **kwargs,
                "texture": arcade.load_texture(
                    C.MENU.PREVIEW_BASEPATH / f"{self.map_name}.png",
                ),
                "texture_hovered": hovered,
                "text": self.label,
            },
        )
        self.scale(1 / (1024 / 320))  # to get 1024x567 preview image
