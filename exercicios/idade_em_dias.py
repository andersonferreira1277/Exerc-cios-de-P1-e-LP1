#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Leia um valor inteiro correspondente � idade de uma pessoa em dias e informe-a em anos, meses e dias.
Obs.: apenas para facilitar o c�lculo, considere todo ano com 365 dias e todo m�s com 30 dias

Formato de entrada
O arquivo de entrada cont�m um valor inteiro.

Formato de sa�da
Imprima a sa�da conforme exemplo fornecido.
"""
ano = 0
mes = 0
dia = 0
def contar(d):
    global ano
    global mes
    global dia
    if d > 365:
        ano = d/365
        d = d%365
    if d > 30:
        mes = d/30
        d = d % 30
    dia = d

d = int(input())
contar(d)
print ("%d ano(s)" % ano)
print ("%d mes(es)" % mes)
print ("%d dia(s)" % dia)