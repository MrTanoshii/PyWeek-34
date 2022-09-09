import arcade
import src.const as C
from .resource import Resource


class Gold(Resource):
    """The base class for the Gold resource."""

    value_current: int = C.RESOURCES.DEFAULT_GOLD

    @classmethod
    def reset(cls):
        """Reset the resource value to the default value."""
        cls.value_current = C.RESOURCES.DEFAULT_GOLD

    @classmethod
    def draw(cls):
        arcade.draw_text(
            f"Gold: {cls.get()}",
            C.GUI.PADDING,
            C.GUI.PADDING,
            C.GUI.GOLD_COLOR,
            C.GUI.RESOURCE_FONT_SIZE,
        )
