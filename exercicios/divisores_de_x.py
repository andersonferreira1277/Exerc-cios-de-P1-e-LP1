#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Escreva um programa que receba como entrada um número inteiro positivo e exiba todos os divisores positivos dele em ordem decrescente.

Formato de entrada
Um número inteiro positivo

Formato de saída
Vários números inteiros separados por quebra de linha
"""
num = int(input())
for i in range(num,0,-1):
    if num % i == 0:
        print i