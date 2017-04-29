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

N�mero primo, � um n�mero p cujo conjunto dos divisores n�o invers�veis n�o � vazio, e todos os seus elementos s�o produtos de p por n�meros inteiros invers�veis. De acordo com esta defini��o, 0, 1 e -1 n�o s�o n�meros primos.
"""
#============================fun��o==================================
import math
def primos(num):
    dividido = 0
    num_sqrt = num
    num_sqrt = math.sqrt(num_sqrt)
    num_sqrt = math.ceil(num_sqrt)
    num_sqrt = int(num_sqrt)
    for i in range(1,num_sqrt+1):
        teste = num%i
        if teste == 0:
            dividido += 1
            if dividido >=2:
                break
    if dividido >= 2:
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
    if (i == 0) or (i == 1):
        print (0)
    elif (i == 2):
        print(1)
    else:
        print(primos(i))