#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Fa�a um programa que leia um hor�rio no sistema de 24 horas e imprima este hor�rio no sistema de 12 horas.
Obs: o valor m�nimo de um dia � 00:00 e o m�ximo � 23:59.

Formato de entrada
Consiste de 2 valores inteiros indicando as horas e os minutos.

Formato de sa�da


Consiste de dois valores indicando as horas e os minutos no sistema de 12 horas e uma linha contendo "am" ou "pm" (sem aspas) para que o hor�rio de sa�da seja compat�vel com o de entrada.
Caso o valor recebido seja exatamente meia noite, ele ser� dado como
00
00
e a sa�da esperada �:
12
00
am
Caso o valor recebido seja exatamente meio dia, ele ser� dado como:
12
00
e a sa�da esperada �:
12
00
pm
IMPORTANTE: se voc� receber,, por exemplo:
15
05
Voc� deve imprimir:
03
05
pm
e n�o:
3
5
pm
ou seja, � importante que voc� imprima o zero � esquerda.
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