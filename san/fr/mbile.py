import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text="Tech With Tim")
    
if _name_ == "_main_":
    MyApp().run()
