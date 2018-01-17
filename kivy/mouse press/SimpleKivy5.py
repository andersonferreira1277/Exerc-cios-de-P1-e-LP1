#!/usr/bin/env python3
#-*- coding: utf-8-*-

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('SimpleKivy5.kv')


class TouchInput(Widget):
    
    def on_touch_down(self, touch):
        print(touch.spos)
        
    def on_touch_move(self, touch):
        print(touch)
        
        
class SimpleKivy5(App):

    def build(self):
        return TouchInput()


if __name__ == '__main__':
    SimpleKivy5().run()
