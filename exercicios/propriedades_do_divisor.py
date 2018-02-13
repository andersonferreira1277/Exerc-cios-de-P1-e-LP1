#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Dado um número inteiro 10<=n<=100, faça um programa que imprima SIM caso ele satisfaça as propriedades abaixo ou NAO, caso contrário:
Não termina em zero;
Se o dígito da direita for removido, o número restante é divisor do número original.

Formato de entrada
Um número inteiro entre 10 e 100.

Formato de saída
SIM caso o número satisfaça as propriedades ou NAO, caso contrário.
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