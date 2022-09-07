import src.const as C
from .resource import Resource


class Gold(Resource):
    """The base class for the Gold resource."""

    value_current: int = C.RESOURCES.DEFAULT_GOLD

    @classmethod
    def reset(cls):
        """Reset the resource value to the default value."""
        cls.value_current = C.RESOURCES.DEFAULT_GOLD
