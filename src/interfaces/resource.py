import abc


class ResourceInterface(metaclass=abc.ABCMeta):
    """Interface for Resource classes."""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "increment")
            and callable(subclass.increment)
            or NotImplemented
        )

    def increment(self, change: int):
        """Increment the resource by change."""

        self.value_current = self.value_current + change
        if self.value_current < 0:
            self.value_current = 0
        elif self.value_current > self.value_max:
            self.value_current = self.value_max

    def __init__(self) -> None:
        self.value_current: int = 0
        self.value_max: int = 999999
