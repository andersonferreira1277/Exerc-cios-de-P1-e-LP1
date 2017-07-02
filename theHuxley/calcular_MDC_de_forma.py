#-*- coding: latin1 -*-
#Windows 10 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Dois n�meros naturais sempre t�m divisores comuns. Por exemplo: os divisores comuns de 12 e 18 s�o 1,2,3 e 6. Dentre eles, 6 � o maior. Ent�o chamamos o 6 de m�ximo divisor comum de 12 e 18 e indicamos m.d.c.(12,18) = 6.
Desenvolva uma fun��o recursiva para calcular o m.d.c de dois inteiros.

Dois inteiros positivos.

Um inteiro positivo.

http://www.viniciusviana.com/desenvolvimento/algoritmo-de-euclides-mdc-em-python/
'''
'''
def euclides_mdc(dividendo, divisor): #maximo divisor comum pelo metodo de euclides
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp
    return dividendo
'''
def euclides_recursivo_mdc(dividendo, divisor):
    if divisor == 0:
        return dividendo
    else:
        return euclides_recursivo_mdc(divisor, dividendo % divisor)
n = int(input())
m = int(input())
print euclides_recursivo_mdc(n, m)
