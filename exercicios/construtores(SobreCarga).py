#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class SobreCarga:
    """x = 0
    y = 0"""
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
    def imprimir(self):
        print("X = {}, Y = {}".format(self.x, self.y))

sc1 = SobreCarga();
sc2 = SobreCarga(10,20);
print "Construtor Default"
sc1.imprimir();
print "Construtor Overload"
sc2.imprimir();
raw_input()
