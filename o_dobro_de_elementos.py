#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Você receberá uma sequência de números inteiros e deve imprimir o dobro de cada número recebido.

Formato de entrada
Você receberá um número inteiro n, indicando quantos números virão a seguir. Depois você receberá n linhas, cada uma com um número inteiro. Você deve imprimir o dobro de cada número dessas n linhas.
Considere n<=20

Formato de saída
Você deve imprimir o dobro de cada número, sendo um por linha.
Por exemplo, para a entrada:
3
10
50
110
Você deve imprimir:
20
100
220
"""
count = 1
limite = int(input())
lista = []
while count <= limite:
    lista.append(int(input()))
    count += 1
for i in lista:
    print i*2