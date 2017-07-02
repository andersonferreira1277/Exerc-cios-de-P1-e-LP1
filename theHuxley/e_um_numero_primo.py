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