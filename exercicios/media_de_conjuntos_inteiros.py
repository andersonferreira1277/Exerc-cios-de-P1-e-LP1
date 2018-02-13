#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Considere uma lista de valores inteiros não negativos, separados por espaço, em uma única linha.
Escreva um programa que calcule a média dos valores lidos. A média deve ser impressa com uma casa decimal.

Formato de entrada
Uma lista de valores inteiros não negativos, separados por espaço, em uma única linha.

Formato de saída
Como saída, espera-se a impressão do nome da medida (Media) seguida por um espaço, o sinal de igualdade, outro espaço e o valor calculado com uma casa decimal.
"""
num = map(float, raw_input().split())
print ("Media = %.1f" % (sum(num)/len(num)))