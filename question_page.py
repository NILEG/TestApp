from kivy.lang import Builder
from result import Result
from kivymd.uix.screen import MDScreen
import json
from login import Login
from database import Database
Builder.load_string("""
#:import Custom_ProgressBar customwidgets
<QuestionPage>:
    MDLabel:
        adaptive_size: True
        pos_hint: {"center_x":0.5, "top":0.9}
        text: "Opto App"
        font_size: '64sp'
        font_name: "stylish_font.ttf"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    MDAnchorLayout:
        anchor_x:"center"
        anchor_y:"center"
        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            size_hint_x:0.7
            spacing: dp(10)
            MDLabel:
                id: label
                text: "Are the headaches unilateral or bilateral?"
                font_size: '18sp'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                size_hint_y:None
                height: dp(100)
                pos_hint:{"center_x":0.5}  
            MDRaisedButton:
                id: option1
                elevation: 2
                text: "Option 1"
                padding: [dp(100+(10-len(self.text))),0,dp(100+(10-len(self.text))),0]
                md_bg_color: app.theme_cls.accent_color
                pos_hint:{"center_x":0.5}  
                on_press: root.option_selection(self.text)
            MDRaisedButton:
                id: option2
                elevation: 2
                text: "Option 2"
                padding: [dp(100+(10-len(self.text))),0,dp(100+(10-len(self.text))),0]
                md_bg_color: app.theme_cls.accent_color
                pos_hint:{"center_x":0.5}  
                on_press: root.option_selection(self.text)
    Custom_ProgressBar:
        id: progressbar
        size_hint_x:0.8
        pos_hint:{"center_x":0.5, "y":0.05}    
        progress_value: 50
        label_text: "50%"
        
""")
class QuestionPage(MDScreen):
    data=dict()
    questions=list()
    counter=0
    result = list()
    lst=list()
    @staticmethod
    def set_file(filename):
        file = open(filename)
        QuestionPage.data = json.load(file)
        QuestionPage.questions = QuestionPage.data["Questions"]
        QuestionPage.counter=0
        QuestionPage.lst=[]
        QuestionPage.result=[]
    def on_pre_enter(self, *args):
        self.next_question()
    def next_question(self):
        self.ids.label.text = QuestionPage.questions[QuestionPage.counter]
        self.ids.option1.text = list(QuestionPage.data[QuestionPage.questions[QuestionPage.counter]].keys())[0]
        self.ids.option2.text = list(QuestionPage.data[QuestionPage.questions[QuestionPage.counter]].keys())[1]
        self.ids.progressbar.label_text=str(int((QuestionPage.counter/len(QuestionPage.questions))*100))+"%"
        self.ids.progressbar.progress_value=int((QuestionPage.counter/len(QuestionPage.questions))*100)
    def option_selection(self, key):
        value=QuestionPage.data[QuestionPage.questions[QuestionPage.counter]][key]
        QuestionPage.lst+=value
        if(QuestionPage.counter<len(QuestionPage.questions)-1):
            QuestionPage.counter += 1
            self.next_question()
            print(QuestionPage.counter)
        else:
            self.show_result()
            self.save_history()
            self.manager.current="result_page"
    def show_result(self):
        uniques=set(QuestionPage.lst)
        for unique in uniques:
            percentage=f"{round((QuestionPage.lst.count(unique)/len(QuestionPage.lst))*100, 2)}%"
            QuestionPage.result.append((unique, percentage))
        Result.set_data(QuestionPage.result)
    def save_history(self):
        Database.insert_into_entries(Login.email, QuestionPage.data["Name"])
        entry_id=Database.get_last_entryid(Login.email)
        for item in QuestionPage.result:
            Database.insert_into_data_table(entry_id, Login.email, item[0], item[1])
