#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Escreva um programa que l� um inteiro N (1 <N <1000). Este N � o n�mero de linhas de sa�da impressos por este programa.

Formato de entrada
O arquivo de entrada cont�m um n�mero inteiro N.

Formato de sa�da
Imprima a sa�da de acordo com o exemplo dado.
"""
a = int(input())
linha = 1
for i in range(1,a+1):
    print ("%d %d %d" % (i,i**2,i**3))