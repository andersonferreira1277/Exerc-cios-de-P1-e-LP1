#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Faça um programa que dado um número indique se ele é um primo ou não.

Formato de entrada
Você irá receber uma sequência de números separados por um final de linha. A entrada termina quando o número lido for -1.

Formato de saída
Para cada número lido você deve imprimir 0 caso o número não seja primo ou 1 caso seja.
Depois de cada 0 ou 1 impresso, coloque um final de linha.
"""
"""

Para ganhar tempo, teste apenas até sqrt(n), arredondando para cima.
Testar todos os números entre 2 e n-1 pode demorar bastante.
Por exemplo, se fossemos verificar se o 103 é primo usando esse método, precisaríamos dividir ele por 3, 4, 5 ,6 ... etc.. até o 102! Por sorte, não é necessário dividir por todos esses fatores. Só é necessário dividir pelos divisores que estão entre 2 e a raiz de n.
Se a raiz de n não for um número inteiro, arredonde para cima e teste até esse número.

Número primo, é um número p cujo conjunto dos divisores não inversíveis não é vazio, e todos os seus elementos são produtos de p por números inteiros inversíveis. De acordo com esta definição, 0, 1 e -1 não são números primos.
"""
#============================função==================================
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