#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Dada duas listas encadeadas A e B, escreva uma fun��o para verificar se B � um subconjunto de A.

Formato de entrada
A primeira linha de entrada ser� o tamanho da primeira lista (n�mero inteiro). Em seguida, uma lista com n n�meros inteiros. A terceira linha de entrada � o tamanho da segunda lista (n�mero inteiro). Por fim, uma lista com m n�meros inteiros. Nesse caso, m e n podem assumir valores iguais ou diferentes.

Formato de sa�da
0 caso n�o seja subconjunto; 1 caso contr�rio.
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