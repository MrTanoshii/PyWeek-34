import src.const as C
from .resource import Resource


class Research(Resource):
    """The base class for Resource Research."""

    value_current: int = C.RESOURCES.DEFAULT_RESEARCH

    @classmethod
    def reset(cls):
        """Reset the resource value to default value."""
        cls.value_current = C.RESOURCES.DEFAULT_RESEARCH
