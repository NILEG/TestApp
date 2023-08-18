import threading

from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from plyer import filechooser
from summary import Summarizer
Builder.load_string("""
<Home>:
    MDBoxLayout:
        orientation: "vertical"
        MDAnchorLayout:
            anchor_x:"center"
            anchor_y:"top"
            size_hint_y:None
            height: dp(200)
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                MDIconButton:
                    icon: "file-upload"
                    icon_size:'150sp'
                    adaptive_size: True
                    pos_hint: {"center_x":0.5}
                    on_press: root.upload_file()
                MDLabel:
                    text: "Get the [b]crux![/b]"
                    markup: True
                    halign: "center"
        MDBoxLayout:
            size_hint_y:0.6
            orientation: "vertical"
            padding: dp(20)
            MDAnchorLayout:
                anchor_y: "top"
                size_hint_y:None
                height: dp(80)
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_size: True
                    MDLabel:
                        text: "Length:"
                        size_hint:None,None
                        width: dp(250)
                        height: dp(30)
                        padding: dp(15),0
                    MDSlider:
                        size_hint:None,None
                        width: dp(250)
                        height: dp(30)
            MDScrollView:
                MDLabel:
                    adaptive_height: True
                    id: label
                    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    MDBoxLayout:
        adaptive_size: True
        pos_hint: {"right": 1}
        padding: dp(10)
        MDFloatingActionButton:
            icon: "content-copy"
            
""")
class Home(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tool=Summarizer()
    def upload_file(self):
        file=filechooser.open_file(title="Choose PDF File", filters=[("*.pdf")])
        thread=threading.Thread(target=self.getsummary, args=[file[0]])
        thread.start()
    def getsummary(self, file):
        summary=self.tool.summary(file)
        self.ids.label.text=summary


