#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Dado um n�mero inteiro 10<=n<=100, fa�a um programa que imprima SIM caso ele satisfa�a as propriedades abaixo ou NAO, caso contr�rio:
N�o termina em zero;
Se o d�gito da direita for removido, o n�mero restante � divisor do n�mero original.

Formato de entrada
Um n�mero inteiro entre 10 e 100.

Formato de sa�da
SIM caso o n�mero satisfa�a as propriedades ou NAO, caso contr�rio.
"""
a = int(input())
b = a/10
if (a < 10) or (a > 100):
    print ("NAO")
elif a%10 == 0:
    print ("NAO")
elif a%b == 0:
    print ("SIM")
else:
    print ("NAO")