import arcade
import src.const as C
from .resource import Resource


class Score(Resource):
    """The base class for the Score resource."""

    value_current: int = 0

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
        cls.value_current = 0

    @classmethod
    def draw(cls):
        arcade.draw_text(
            f"Score: {cls.get()}",
            C.GUI.PADDING,
            C.GUI.PADDING * 4,
            C.GUI.SCORE_COLOR,
            C.GUI.RESOURCE_FONT_SIZE,
        )
