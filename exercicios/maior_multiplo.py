#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Seu objetivo é determinar o maior múltiplo de um inteiro dado menor do que ou igual a um outro inteiro dado

Formato de entrada
Consiste de dois inteiros positivos M e N.

Formato de saída
A saída consiste do maior número que seja múltiplo de M e menor que N, se não houver um múltiplo de M menor que N você deve imprimir "sem multiplos menores que N", sem as aspas, onde N deve ser substituído pelo valor de entrada N.
"""
a = int(input())
b = int(input())
resultado = 0
count = 1
for i in range(1,b+1):
    if i%a == 0:
        resultado = i
if resultado == 0:
    print ("sem multiplos menores que %d" % b)
elif b < a:
    print ("sem multiplos menores que %d" % b)
else:
    print (resultado)