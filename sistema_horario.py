#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Faça um programa que leia um horário no sistema de 24 horas e imprima este horário no sistema de 12 horas.
Obs: o valor mínimo de um dia é 00:00 e o máximo é 23:59.

Formato de entrada
Consiste de 2 valores inteiros indicando as horas e os minutos.

Formato de saída


Consiste de dois valores indicando as horas e os minutos no sistema de 12 horas e uma linha contendo "am" ou "pm" (sem aspas) para que o horário de saída seja compatível com o de entrada.
Caso o valor recebido seja exatamente meia noite, ele será dado como
00
00
e a saída esperada é:
12
00
am
Caso o valor recebido seja exatamente meio dia, ele será dado como:
12
00
e a saída esperada é:
12
00
pm
IMPORTANTE: se você receber,, por exemplo:
15
05
Você deve imprimir:
03
05
pm
e não:
3
5
pm
ou seja, é importante que você imprima o zero à esquerda.
"""
import math
hora = int(input())
minutos = int(input())
pm_am = ""
if hora > 11 and hora != 12:
    pm_am = "pm"
    hora = int(math.fabs(hora - 12))
elif hora == 12:
    pm_am = "pm"
elif hora <10:
    pm_am = "am"
    if hora == 0:
        hora = 12
print (str(hora).zfill(2))
print (str(minutos).zfill(2))
print (pm_am)