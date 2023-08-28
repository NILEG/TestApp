from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<Result>:
    MDTopAppBar:
        pos_hint: {"top":1}
        md_bg_color: app.theme_cls.accent_light
        left_action_items: [["arrow-left-bold", lambda x: root.back()]]
        specific_text_color: app.theme_cls.primary_color
        elevation: 0
        
    MDLabel:
        adaptive_size: True
        pos_hint: {"center_x":0.5, "top":0.9}
        text: "Opto App"
        font_size: '64sp'
        font_name: "stylish_font.ttf"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    MDBoxLayout:
        id: placeholder
        spacing: dp(10)
        padding: dp(30)
        orientation: "vertical"
        MDLabel:
            text: "Result"
            adaptive_size: True
            pos_hint: {"center_x":0.5}
            font_size: '18sp'
            bold: True
""")
class Result(MDScreen):
    row_data=list()
    @staticmethod
    def set_data(data):
        Result.row_data=data
    def on_pre_enter(self, *args):
        self.ids.placeholder.clear_widgets()
        column_data=[("Name", dp(40)), ("Percentage", dp(30))]
        data_table = MDDataTable(column_data=column_data, row_data=Result.row_data,
                                 size_hint=(None,None), size=(dp(350), dp(400)),
                                      pos_hint={"center_x": 0.5}, elevation=2,
                                      background_color_header="#E91E63",
                                      rows_num=20)
        self.ids.placeholder.add_widget(data_table)
    def back(self):
        self.manager.current="home"
