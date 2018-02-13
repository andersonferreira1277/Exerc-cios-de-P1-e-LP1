#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Escreva um programa que receba como entrada 5 números inteiros positivos, e exiba a soma dos fatoriais daqueles que são múltiplos de 3.

Formato de entrada
Números inteiros

Formato de saída
Um número inteiro
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