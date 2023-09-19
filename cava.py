from kivy.app import App
from kivy.core.window import Window
from kivy.uix.bubble import  Widget
from kivy.graphics import Canvas,Color,Rectangle


Window.size=(400,300)

class MyApp(App):

    def build(self):
        w=Widget()
        with w.canvas:
            Color(1,1,1,1)
            Rectangle(pos=[150,140],sise=[200,100])
        return w

if __name__ == '__main__':
    MyApp().run()
