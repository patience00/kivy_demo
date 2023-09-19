from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import  FloatLayout
from kivy.metrics import Metrics
print(Metrics.density)
print(Metrics.dpi)

width=500
height=500
Window.size=(width,height)

class MyApp(App):

    def build(self):
        layout=FloatLayout()
        # btn=Button(text="click me111",pos=[0,0],size_hint_max=(width*Metrics.density,height*Metrics.density),on_press=lambda  e:print("bubbbbbb"))
        btn=Button(text="",
                   pos=[0,0],
                   font_size=20,
                   size_hint_max=("400dp","200dp"),
                   background_down='./img/2.png',
                   background_normal='./img/3.png',
                   # background_color=(66,99,100,1),
                   on_press=lambda  e:print("bubbbbbb"))
        layout.add_widget(btn)
        return layout


if __name__ == '__main__':
    MyApp().run()
