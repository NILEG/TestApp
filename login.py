from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from database import Database

Builder.load_string("""
#:import CustomTextField customwidgets
<Login>:
    MDBoxLayout:
        orientation: "vertical"
        spacing:dp(75)
        padding: dp(50)
        MDBoxLayout:
            size_hint_y:0.35
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
                    elevation: 0
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
                MDBoxLayout:
                    adaptive_size:True
                    pos_hint: {"right":1}
                    padding: [0,dp(20),0,0]
                    spacing: dp(20)
                    MDFlatButton:
                        elevation: 0
                        text: "Sign up"
                        on_press: root.to_signup()
                    MDRaisedButton:
                        elevation: 0
                        text: "Login"
                        on_press: root.login()
                    
                    
        
""")
class Login(MDScreen):
    email=""
    def login(self):
        if(Database.isExist(self.ids.email.text, self.ids.password.ids.textfield.text)):
            self.manager.current="home"
            Login.email=self.ids.email.text
        else:
            print("Invalid Information")

    def to_signup(self):
        self.manager.current="signup"