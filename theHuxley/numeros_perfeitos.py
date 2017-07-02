#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Um n�mero inteiro � dito perfeito se o dobro dele � igual � soma de todos os seus divisores.
Por exemplo, como os divisores de 6 s�o 1, 2, 3 e 6 e 1 + 2 + 3 + 6 = 12, 6 � perfeito.
A matem�tica ainda n�o sabe se a quantidade de n�meros perfeitos � ou n�o finita. Escreva um programa que liste todos os n�meros perfeitos menores que um inteiro n dado.

Formato de entrada
Um inteiro n.

Formato de sa�da
Um lista de n�meros inteiros perfeitos em ordem crescente separados por um final de linha.
"""
def divi(num):
    divisor = []
    for i in range(1,num+1):
        if num%i == 0:
            divisor.append(i)
    return divisor

a = int(input())
for i in range(1,a):
    b = sum(divi(i))
    if i*2 == b:
        print (i)