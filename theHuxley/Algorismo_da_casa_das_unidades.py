#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o

Escreva um programa que recebe um numero inteiro como entrada e fornece o algarismo da casa das unidades deste numero.

Por exemplo, o algarismo da casa das unidades do n�mero 3872 � 2.

Se o n�mero dado for negativo, considere que o algarismo tamb�m ser� negativo. Por exemplo, se o n�mero dado for -74, a resposta deve ser -4 e n�o 4.

Formato de entrada

Um n�mero inteiro

Formato de sa�da

Um inteiro representando o algarismo da casa das unidades.
"""
numero  = int(input())
if numero >= 0:
    numero = numero%10
else:
    numero = numero%-10
print (numero)