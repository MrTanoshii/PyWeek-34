from typing import Optional


class ViewsStack:
    VIEWS_STACK = []

    @classmethod
    def push(cls, view: type):
        cls.VIEWS_STACK.append(view)

    @classmethod
    def pop(cls) -> Optional[type]:
        if cls.VIEWS_STACK:
            return cls.VIEWS_STACK.pop(0)
