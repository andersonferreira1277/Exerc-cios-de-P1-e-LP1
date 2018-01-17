#!/usr/bin/env python3
#-*- coding: utf-8-*-

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


Builder.load_file('SimpleKivy4.kv')


class SimpleKivy2(App):

    def build(self):
        return FloatLayout()


if __name__ == '__main__':
    SimpleKivy2().run()
