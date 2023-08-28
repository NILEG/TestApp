from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from question_page import QuestionPage
from database import Database
from login import Login
from customwidgets import CustomItem
Builder.load_string("""
<Home>:
    MDTopAppBar:
        pos_hint: {"top":1}
        md_bg_color: app.theme_cls.accent_light
        right_action_items: [["logout", lambda x: root.logout()]]
        specific_text_color: app.theme_cls.primary_color
        elevation: 0
    MDBottomNavigation:
        id: navigation
        on_size: self.switch_tab("home")
        MDBottomNavigationItem:
            name: "account"
            icon: "account-circle"
            text: "Account"
            on_tab_press: root.get_account_info()
            MDBoxLayout:
                orientation: "vertical"
                MDLabel:
                    adaptive_height: True
                    text: "Opto App"
                    halign: "center"
                    font_size: '64sp'
                    font_name: "stylish_font.ttf"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                
                MDAnchorLayout:
                    anchor_x:"center"
                    anchor_y: "center"
                    MDBoxLayout:
                        orientation:"vertical"
                        adaptive_height: True
                        size_hint_x:None
                        width: dp(300)
                        MDLabel:
                            text: "Personal Information"
                            adaptive_height: True
                            halign: "center"
                        MDTextField:
                            id: name
                            hint_text: "Name"
                        MDTextField:
                            id: email
                            hint_text: "Email"
                            readonly: True
                        MDTextField:
                            id: password
                            hint_text: "Password"
                        MDRaisedButton:
                            text: "Update"
                            padding: [dp(20),0,dp(20),0]
                            pos_hint: {"right":1}
                            on_press: root.update()
                    
        MDBottomNavigationItem:
            name: "home"
            icon: "home-account"
            text: "Home"
            MDBoxLayout:
                orientation: "vertical"
                spacing: dp(20)
                MDLabel:
                    adaptive_height: True
                    text: "Opto App"
                    halign: "center"
                    font_size: '64sp'
                    font_name: "stylish_font.ttf"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                MDAnchorLayout:
                    anchor_x:"center"
                    anchor_y:"top"
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: dp(30)
                        adaptive_width: True
                        padding: 0,0,0,dp(70) #Avoid overlapping with the BottomNavigationMenu
                        MDLabel:
                            text: "Available Options"
                            adaptive_height: True
                            halign: "center"
                        MDScrollView:
                            size_hint_x:None
                            width: dp(300)
                            pos_hint:{"center_x":0.5}
                            MDGridLayout: 
                                adaptive_height: True
                                spacing: dp(20)
                                padding: dp(20)
                                cols: 2
                                DCard:
                                    name: "Headache"
                                    icon_name: "head-plus"
                                    on_press: root.headache()
                                DCard:
                                    name: "Eye Flash"
                                    icon_name: "flash-red-eye"
                                    on_press: root.flashes()
                                DCard:
                                    name: "Red Eye"
                                    icon_name: "eye"
                                DCard:
                                    name: "Other diseases"
                                    icon_name: "plus"
        MDBottomNavigationItem:
            name: "history"
            icon: "history"
            text: "History"
            on_tab_press:root.gethistory()
            MDBoxLayout:
                orientation: "vertical"
                spacing: dp(20)
                padding: dp(20),0,dp(20),dp(70) #Avoid overlapping with the BottomNavigationMenu
                MDLabel:
                    adaptive_height: True
                    text: "History"
                    halign: "center"
                    font_size: '24sp'
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                MDScrollView:
                    MDList:
                        id: list
                
                
""")
class Home(MDScreen):
    def on_pre_enter(self, *args):
        self.ids.navigation.switch_tab("home")
    def update(self):
        Database.update_information(self.ids.name.text, self.ids.email.text, self.ids.password.text)
    def get_account_info(self):
        result=Database.getUserInfo(Login.email)
        self.ids.name.text=result[2]
        self.ids.email.text=result[0]
        self.ids.password.text=result[1]
    def gethistory(self):
        self.ids.list.clear_widgets()
        results=Database.get_all_entries(Login.email)
        for result in results:
            list_item=CustomItem(text=result[-1], entry_id=result[0])
            list_item.bind(on_press=self.show_details)
            self.ids.list.add_widget(list_item)
    def logout(self):
        self.manager.current="login"
    def flashes(self):
        QuestionPage.set_file("flashes.json")
        self.manager.current = "question_page"
    def headache(self):
        QuestionPage.set_file("headache.json")
        self.manager.current="question_page"
    def show_details(self, obj):
        content=MDBoxLayout(orientation="vertical", adaptive_size=True)
        column_data = [("Name", dp(40)), ("Percentage", dp(30))]
        data=Database.get_data(Login.email, obj.entry_id)
        row_data=[]
        for item in data:
            row_data.append((item[-2], item[-1]))
        data_table = MDDataTable(column_data=column_data, row_data=row_data,
                                 size_hint=(None, None), size=(dp(350), dp(400)),
                                 pos_hint={"center_x": 0.5}, elevation=2,
                                 background_color_header="#E91E63",
                                 rows_num=20)
        content.add_widget(data_table)
        MDDialog(title="Details", type="custom", size_hint=(None, None), size=(dp(400), dp(440)),content_cls=content).open()
