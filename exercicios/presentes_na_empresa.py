#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Édipo ficou encarregado de comprar presentes para os funcionários da empresa. Cada funcionária vai ganhar uma garrafa de vinho, que custa R$ 10, e cada funcionário ganhará um panetone, que custa R$ 8,50. Escreva um programa que receba como entrada a quantidade de mulheres e a quantidade de homens que trabalham na empresa, e exiba o valor total gasto com presentes, e também o valor médio gasto com cada funcionário.

Formato de entrada
Dois valores inteiros (atenção para a sequência indicada no enunciado)

Formato de saída
Dois valores reais com duas casas decimais cada (atenção para a sequência indicada no enunciado)
"""
mulheres = int(input())
homens = int(input())
t = mulheres*10 + homens*8.50
print ("%.2f" % (t))
print ("%.2f" % (t/(mulheres+homens)))