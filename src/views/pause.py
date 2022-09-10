import arcade.gui
from src.gui.window import Menu


class PauseView(arcade.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.manager = arcade.gui.UIManager()
        self.manager.add(Menu())

    def on_show_view(self):
        pass
