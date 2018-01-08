#!/usr/bin/env python3
#-*- coding: utf-8-*-

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text='Hello World!!!')


if __name__ == '__main__':
    app = MyApp()
    app.run()
