from kivy.app import App
from kivy.core.window import Window
from kivy.uix.bubble import  Button


Window.size=(400,300)

class MyApp(App):

    def build(self):
        return Button(text="click me",on_press=lambda  e:print("bubbbbbb"))

if __name__ == '__main__':
    MyApp().run()
