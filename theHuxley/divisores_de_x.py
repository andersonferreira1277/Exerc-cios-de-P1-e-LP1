#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Escreva um programa que receba como entrada um n�mero inteiro positivo e exiba todos os divisores positivos dele em ordem decrescente.

Formato de entrada
Um n�mero inteiro positivo

Formato de sa�da
V�rios n�meros inteiros separados por quebra de linha
"""
num = int(input())
for i in range(num,0,-1):
    if num % i == 0:
        print i