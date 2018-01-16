#!/usr/bin/env python3
#-*- coding: utf-8-*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file('MyLabel.kv')
class MyLabel(Label): pass


class MyApp(App):

    def build(self):
        return MyLabel()


if __name__ == '__main__':
    MyApp().run()
