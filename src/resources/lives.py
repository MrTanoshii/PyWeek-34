import arcade
import src.const as C
from .resource import Resource


class Lives(Resource):
    """The base class for the Lives resource."""

    value_current: int = C.RESOURCES.DEFAULT_LIVES

    @classmethod
    def increment(cls, change: int):
        """Takes away lives, then you die"""
        cls.value_current += change
        if cls.value_current < 1:
            # TODO: die
            ...

    @classmethod
    def reset(cls):
        """Reset the resource value to the default value."""
        cls.value_current = C.RESOURCES.DEFAULT_LIVES

    @classmethod
    def draw(cls):
        arcade.draw_text(
            f"Lives: {cls.get()}",
            C.GUI.PADDING,
            C.GUI.PADDING * 2.5,
            C.GUI.LIVES_COLOR,
            C.GUI.RESOURCE_FONT_SIZE,
        )
        