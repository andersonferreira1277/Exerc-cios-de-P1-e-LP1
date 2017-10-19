#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica e informe-o expresso no formato horas:minutos:segundos.

Formato de entrada
O arquivo de entrada contém um valor inteiro N.

Formato de saída
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