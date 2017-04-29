#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Escreva um programa que lê um inteiro N (1 <N <1000). Este N é o número de linhas de saída impressos por este programa.

Formato de entrada
O arquivo de entrada contém um número inteiro N.

Formato de saída
Imprima a saída de acordo com o exemplo dado.
"""
a = int(input())
linha = 1
for i in range(1,a+1):
    print ("%d %d %d" % (i,i**2,i**3))