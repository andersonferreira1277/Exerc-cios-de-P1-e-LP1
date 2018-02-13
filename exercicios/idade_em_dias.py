#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias.
Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias

Formato de entrada
O arquivo de entrada contém um valor inteiro.

Formato de saída
Imprima a saída conforme exemplo fornecido.
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