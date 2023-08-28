from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from database import Database

Builder.load_string("""
#:import CustomTextField customwidgets
<Signup>:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(50)
        MDBoxLayout:
            size_hint_y:0.25
            MDLabel:
                text: "Opto App"
                halign: "center"
                font_size: '64sp'
                font_name: "stylish_font.ttf"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
        MDAnchorLayout:
            anchor_x: "center"
            anchor_y: "top"
            MDBoxLayout:
                adaptive_size: True
                orientation: "vertical"
                MDTextField:
                    id: name
                    size_hint_x:None
                    width: dp(300)
                    hint_text: "Name"
                MDTextField:
                    id: email
                    size_hint_x:None
                    width: dp(300)
                    hint_text: "Email"
                    validator: "email"
                    error_color: app.theme_cls.primary_light
                CustomTextField:
                    id: password
                    size_hint_x:None
                    width: dp(300)
                    _hint: "Password"
                CustomTextField:
                    id: cpassword
                    size_hint_x:None
                    width: dp(300)
                    _hint: "Confirm Password"
                MDBoxLayout:
                    padding: [0, dp(20),0,0]
                    pos_hint: {"right":1}
                    adaptive_size: True
                    MDRaisedButton:
                        text: "Signup"
                        on_press: root.signup()
                        



""")
class Signup(MDScreen):
    def signup(self):
        if(Database.isValid(self.ids.email.text) and self.ids.password.ids.textfield.text==self.ids.cpassword.ids.textfield.text and self.ids.email.text!=""):
            Database.insert_into_users(self.ids.email.text, self.ids.password.ids.textfield.text, self.ids.name.text)
            print(self.ids.email.text, self.ids.password.ids.textfield.text, self.ids.name.text)
            self.manager.current="login"
        else:
            print("Email already exsist or Passwords doesn't match")
