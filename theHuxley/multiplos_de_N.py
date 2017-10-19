#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Escrever programa para exibir os m�ltiplos de N contidos entre os valores A e B, sendo N, A e B definidos pelo utilizador.

Formato de entrada
Tr�s valores inteiros.  Cada um em uma linha distinta.  O primeiro valor, N,  corresponde ao n�mero do qual se deseja verificar se h� m�ltiplos.  Os outros dois valores, A e B inclusivos, correspondem aos limites do intervalo de valores a serem validados como m�ltiplos ou n�o de N.

Formato de sa�da
Valores contidos entre A e B, que sejam m�ltiplos de N.
Caso n�o haja m�ltiplos de N, entre A e B, exibir: INEXISTENTE.
"""
n = int(input())
a = int(input())
b = int(input())
resultado = []
for i in range(a,b+1):
    if i % n == 0:
        resultado.append(i)
    else:
        continue
if resultado == []:
    print ("INEXISTENTE")
else:
    for x in resultado:
        print x