#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Leia um valor inteiro, que � o tempo de dura��o em segundos de um determinado evento em uma f�brica e informe-o expresso no formato horas:minutos:segundos.

Formato de entrada
O arquivo de entrada cont�m um valor inteiro N.

Formato de sa�da
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""
horas = 0
minutos = 0
segundos = 0
def conversor(s):
    global horas
    global minutos
    global segundos
    if s >= 3600:
        horas = s/3600
        s = s%3600
    if s >= 60:
        minutos = s/60
        s = s%60
    segundos = s
s = int(input())
conversor(s)
print ("%d:%d:%d" % (horas,minutos,segundos))