#-*- coding: latin1 -*-
#Windows 10 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Fa�a uma fun��o recursiva que receba um n�mero inteiro positivo par N e imprima todos os n�meros pares de 0 at� N em ordem crescente.

Um inteiro positivo N.

Uma sequ�ncia de n�meros de 0 � N linha � linha.
'''
def par(n):
    if n%2 == 0:
        print n
    n -= 1
    if n >= 0:
        par(n)
n = int(input())
par(n)