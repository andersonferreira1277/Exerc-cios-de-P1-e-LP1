#-*- coding: latin1 -*-
#Windows 10 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.

Um inteiro positivo N.

Uma sequência de números de 0 à N linha à linha.
'''
def par(n):
    if n%2 == 0:
        print n
    n -= 1
    if n >= 0:
        par(n)
n = int(input())
par(n)