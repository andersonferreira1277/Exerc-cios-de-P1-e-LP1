#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Faça um programa que leia dois valores inteiros (x e y) e imprima na tela o resultado das seguintes comparações entre estes dois valores, exatamente nesta ordem:
x é maior que y
x é igual a y
x é menor que y
x é diferente de y
x é maior ou igual a y
x é menor ou igual a y

Formato de entrada
Dois números inteiros separados por um fim de linha, representando os valores que serão comparados.

Formato de saída
6 valores, cada um deles separados por um fim de linha, seguindo o modelo do Exemplo de Saída. Os valores possíveis são 0 ou 1. O valor 0 deve ser utilizado para indicar que o resultado da comparação é falsa. O valor 1 deve ser utilizado para indicar que o resultado da comparação é verdadeira.
Obs.: Não esqueça de imprimir o fim de linha após o resultado.
"""
x = int(input())
y = int(input())
print int(x > y)
print int(x == y)
print int(x < y)
print int(x != y)
print int(x >= y)
print int(x <= y)