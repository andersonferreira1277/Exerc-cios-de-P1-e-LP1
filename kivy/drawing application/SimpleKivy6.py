#!/usr/bin/env python3
# -*- coding: utf-8-*-

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.lang import Builder


# Builder.load_file('SimpleKivy6.kv')


class DrawInput(Widget):
    
    def on_touch_down(self, touch):
        print(touch.spos)
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
        
    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)
        
    def on_touch_up(self, touch):
        print("RELEASED!", touch)
        
        
class SimpleKivy6(App):

    def build(self):
        return DrawInput()


if __name__ == '__main__':
    SimpleKivy6().run()
