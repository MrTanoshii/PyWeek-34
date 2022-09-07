class Resource:
    """Parent class for resource subclasses."""

    value_current: int = 0
    value_max: int = 999999

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Resource, cls).__new__(cls)
        return cls.instance

    @classmethod
    def increment(cls, change: int):
        """Increment the resource by change."""
        cls.value_current += change
        if cls.value_current < 0:
            cls.value_current = 0
        elif cls.value_current > cls.value_max:
            cls.value_current = cls.value_max

    @classmethod
    def reset(cls):
        """Reset the resource value to 0."""
        cls.value_current = 0

    @classmethod
    def get(cls):
        return cls.value_current

    @classmethod
    def set(cls, value: int):
        cls.value_current = value
