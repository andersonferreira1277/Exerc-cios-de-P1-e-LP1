#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Seu objetivo � determinar o maior m�ltiplo de um inteiro dado menor do que ou igual a um outro inteiro dado

Formato de entrada
Consiste de dois inteiros positivos M e N.

Formato de sa�da
A sa�da consiste do maior n�mero que seja m�ltiplo de M e menor que N, se n�o houver um m�ltiplo de M menor que N voc� deve imprimir "sem multiplos menores que N", sem as aspas, onde N deve ser substitu�do pelo valor de entrada N.
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