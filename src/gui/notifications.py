import arcade
from src import const as C


class Notification(arcade.Text):
    def __init__(self, *args, **kwargs):
        self.ttl = kwargs.pop(
            "ttl",
            C.NOTIFICATIONS.TIME_TO_LIVE_SEC,
        )  # time to live for notification
        self.start_ttl = self.ttl
        super().__init__(*args, **kwargs)

    def update(self, delta_time: float):
        self.ttl -= delta_time
        self.color = (
            self.color[0],
            self.color[1],
            self.color[2],
            int((self.ttl / self.start_ttl) * 255),
        )


class Notifications:
    _instance = None  # singleton

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.notifications = []

    def create(self, text: str, x: float, y: float, color: arcade.Color):
        if len(self.notifications) >= C.NOTIFICATIONS.MAX_AMOUNT:
            self.notifications.pop(0)
        self.notifications.append(
            Notification(text=text, start_x=x, start_y=y, color=color)
        )

    def update(self, delta_time: float):
        to_delete = []

        for notification in self.notifications:
            notification.update(delta_time)
            if notification.ttl <= 0:
                to_delete.append(notification)

        for notification in to_delete:
            self.notifications.remove(notification)

    def draw(self):
        for notification in self.notifications:
            notification.draw()
