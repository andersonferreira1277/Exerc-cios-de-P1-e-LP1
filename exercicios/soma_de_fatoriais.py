#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Escreva um programa que receba como entrada 5 n�meros inteiros positivos, e exiba a soma dos fatoriais daqueles que s�o m�ltiplos de 3.

Formato de entrada
N�meros inteiros

Formato de sa�da
Um n�mero inteiro
"""
from math import factorial
count = 1
lista = []
resultado = []
while count <= 5:
    num = int(input())
    if num % 3 == 0:
        lista.append(num)
    count += 1
for i in lista:
    resultado.append(factorial(i))
print sum(resultado)