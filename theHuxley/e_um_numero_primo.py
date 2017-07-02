#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Fa�a um programa que dado um n�mero indique se ele � um primo ou n�o.

Formato de entrada
Voc� ir� receber uma sequ�ncia de n�meros separados por um final de linha. A entrada termina quando o n�mero lido for -1.

Formato de sa�da
Para cada n�mero lido voc� deve imprimir 0 caso o n�mero n�o seja primo ou 1 caso seja.
Depois de cada 0 ou 1 impresso, coloque um final de linha.
"""
"""

Para ganhar tempo, teste apenas at� sqrt(n), arredondando para cima.
Testar todos os n�meros entre 2 e n-1 pode demorar bastante.
Por exemplo, se fossemos verificar se o 103 � primo usando esse m�todo, precisar�amos dividir ele por 3, 4, 5 ,6 ... etc.. at� o 102! Por sorte, n�o � necess�rio dividir por todos esses fatores. S� � necess�rio dividir pelos divisores que est�o entre 2 e a raiz de n.
Se a raiz de n n�o for um n�mero inteiro, arredonde para cima e teste at� esse n�mero.
"""
#============================entrada==================================
import math
def primos(num):
    dividido = 0
    num = math.sqrt(num)
    num = math.ceil(num)
    num = int(num)
    for i in range(1,num+1):
        teste = num%i
        if teste == 0:
            dividido += 1
            if dividido >=3:
                break
    if dividido > 2:
        return 0
    elif dividido <= 2:
        return 1
#======================================================================
entrada = input()
lista = []
while entrada != -1:
    if entrada != -1:
        lista.append(entrada)
    entrada = input()
for i in lista:
    print(primos(i))