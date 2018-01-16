#!/usr/bin/env python3
#-*- coding: utf-8-*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('SimpleKivy2.kv')


class Widgets(Widget): pass

class SimpleKivy2(App):

    def build(self):
        return Widgets()


if __name__ == '__main__':
    SimpleKivy2().run()
