#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição

Escreva um programa que recebe um numero inteiro como entrada e fornece o algarismo da casa das unidades deste numero.

Por exemplo, o algarismo da casa das unidades do número 3872 é 2.

Se o número dado for negativo, considere que o algarismo também será negativo. Por exemplo, se o número dado for -74, a resposta deve ser -4 e não 4.

Formato de entrada

Um número inteiro

Formato de saída

Um inteiro representando o algarismo da casa das unidades.
"""
numero  = int(input())
if numero >= 0:
    numero = numero%10
else:
    numero = numero%-10
print (numero)