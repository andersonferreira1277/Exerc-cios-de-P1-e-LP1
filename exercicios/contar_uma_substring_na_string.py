#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Leia duas strings e verifique o n�mero de ocorr�ncias da segunda string na primeira. Exemplo: Se a primeira string digitada for "abracadabra" e a segunda "bra", ent�o o n�mero de ocorr�ncias � 2.

Formato de entrada
Voc� receber� duas linhas. Cada linha com uma string.

Formato de sa�da
Voc� deve imprimir um n�mero inteiro indicando o n�mero de ocorr�ncias encontradas.
Imprima tamb�m o final de linha.
"""
a = raw_input()
b = raw_input()
print a.count(b)
