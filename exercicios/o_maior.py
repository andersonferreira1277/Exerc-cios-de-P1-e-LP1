#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Fa�a um programa que leia tr�s valores e apresente o maior dos tr�s valores lidos seguido da mensagem ?eh o maior?. Utilize a f�rmula:

Formato de entrada
O arquivo de entrada cont�m tr�s valores inteiros.

Formato de sa�da
Imprima o maior dos tr�s valores seguido por um espa�o e a mensagem "eh o maior".
Desafio voc� fazer sem usar "if".
hahahahaha (Risada do mal!)
"""
"""
y = (a + b + abs(a - b)) /2.0;
x = (y + c + abs(y - c)) /2.0; da linguagem C
"""
import math
entrada = raw_input()
entrada = entrada.split()
entrada = map(int, entrada)
y = (entrada[0] + entrada[1] + math.fabs(entrada[0]-entrada[1]))/2
x = (y + entrada[2]+ math.fabs(y-entrada[2]))/2
print ("%d eh o maior" % x)