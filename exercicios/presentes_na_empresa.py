#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
�dipo ficou encarregado de comprar presentes para os funcion�rios da empresa. Cada funcion�ria vai ganhar uma garrafa de vinho, que custa R$ 10, e cada funcion�rio ganhar� um panetone, que custa R$ 8,50. Escreva um programa que receba como entrada a quantidade de mulheres e a quantidade de homens que trabalham na empresa, e exiba o valor total gasto com presentes, e tamb�m o valor m�dio gasto com cada funcion�rio.

Formato de entrada
Dois valores inteiros (aten��o para a sequ�ncia indicada no enunciado)

Formato de sa�da
Dois valores reais com duas casas decimais cada (aten��o para a sequ�ncia indicada no enunciado)
"""
mulheres = int(input())
homens = int(input())
t = mulheres*10 + homens*8.50
print ("%.2f" % (t))
print ("%.2f" % (t/(mulheres+homens)))