#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Voc� receber� uma sequ�ncia de n�meros inteiros e deve imprimir o dobro de cada n�mero recebido.

Formato de entrada
Voc� receber� um n�mero inteiro n, indicando quantos n�meros vir�o a seguir. Depois voc� receber� n linhas, cada uma com um n�mero inteiro. Voc� deve imprimir o dobro de cada n�mero dessas n linhas.
Considere n<=20

Formato de sa�da
Voc� deve imprimir o dobro de cada n�mero, sendo um por linha.
Por exemplo, para a entrada:
3
10
50
110
Voc� deve imprimir:
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