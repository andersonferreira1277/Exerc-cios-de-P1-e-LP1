#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Fa�a um programa que leia dois valores inteiros (x e y) e imprima na tela o resultado das seguintes compara��es entre estes dois valores, exatamente nesta ordem:
x � maior que y
x � igual a y
x � menor que y
x � diferente de y
x � maior ou igual a y
x � menor ou igual a y

Formato de entrada
Dois n�meros inteiros separados por um fim de linha, representando os valores que ser�o comparados.

Formato de sa�da
6 valores, cada um deles separados por um fim de linha, seguindo o modelo do Exemplo de Sa�da. Os valores poss�veis s�o 0 ou 1. O valor 0 deve ser utilizado para indicar que o resultado da compara��o � falsa. O valor 1 deve ser utilizado para indicar que o resultado da compara��o � verdadeira.
Obs.: N�o esque�a de imprimir o fim de linha ap�s o resultado.
"""
x = int(input())
y = int(input())
print int(x > y)
print int(x == y)
print int(x < y)
print int(x != y)
print int(x >= y)
print int(x <= y)