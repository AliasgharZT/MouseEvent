from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder 
from kivy.properties import ObjectProperty

Builder.load_file('mouse.kv')

class Touch(BoxLayout,Widget):
    btn=ObjectProperty()

    def on_touch_down(self,touch):
        print(touch)
        self.btn.opacity=0.5

    def on_touch_up(self,touch):
        print(touch)
        self.btn.opacity=1

    def on_touch_move(self,touch):
        print(touch)

class MainApp(App):
    def build(self):
        return Touch()
    
MainApp().run()

