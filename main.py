from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from database import Database
class Interface(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Database.connect()
class OptoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Pink"
        self.theme_cls.primary_light_hue="400"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.accent_light_hue="50"
        self.theme_cls.accent_hue="700"
        self.theme_cls.material_style="M2"
OptoApp().run()
