#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Considere uma lista de valores inteiros n�o negativos, separados por espa�o, em uma �nica linha.
Escreva um programa que calcule a m�dia dos valores lidos. A m�dia deve ser impressa com uma casa decimal.

Formato de entrada
Uma lista de valores inteiros n�o negativos, separados por espa�o, em uma �nica linha.

Formato de sa�da
Como sa�da, espera-se a impress�o do nome da medida (Media) seguida por um espa�o, o sinal de igualdade, outro espa�o e o valor calculado com uma casa decimal.
"""
num = map(float, raw_input().split())
print ("Media = %.1f" % (sum(num)/len(num)))