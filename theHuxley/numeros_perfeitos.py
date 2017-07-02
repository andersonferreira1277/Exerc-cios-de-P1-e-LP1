#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Um número inteiro é dito perfeito se o dobro dele é igual à soma de todos os seus divisores.
Por exemplo, como os divisores de 6 são 1, 2, 3 e 6 e 1 + 2 + 3 + 6 = 12, 6 é perfeito.
A matemática ainda não sabe se a quantidade de números perfeitos é ou não finita. Escreva um programa que liste todos os números perfeitos menores que um inteiro n dado.

Formato de entrada
Um inteiro n.

Formato de saída
Um lista de números inteiros perfeitos em ordem crescente separados por um final de linha.
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