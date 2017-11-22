#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Dada duas listas encadeadas A e B, escreva uma função para verificar se B é um subconjunto de A.

Formato de entrada
A primeira linha de entrada será o tamanho da primeira lista (número inteiro). Em seguida, uma lista com n números inteiros. A terceira linha de entrada é o tamanho da segunda lista (número inteiro). Por fim, uma lista com m números inteiros. Nesse caso, m e n podem assumir valores iguais ou diferentes.

Formato de saída
0 caso não seja subconjunto; 1 caso contrário.
"""
a = int(input()) #variaveis ignoradas
conjunto1 = raw_input()
b = int(input()) #variaveis ignoradas
conjunto2 = raw_input()
conjunto1 = conjunto1.split()
conjunto2 = conjunto2.split()
conjunto1 = map(int, conjunto1)
conjunto2 = map(int, conjunto2)
r = set(conjunto2).issubset(conjunto1)
if r == True:
    print 1
else:
    print 0