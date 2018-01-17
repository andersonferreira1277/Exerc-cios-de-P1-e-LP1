#!/usr/bin/env python3
#-*- coding: utf-8-*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


Builder.load_file('01(kivy_lang).kv')


class MyApp(App):

    def build(self):
        return Label()


if __name__ == '__main__':
    MyApp().run()
