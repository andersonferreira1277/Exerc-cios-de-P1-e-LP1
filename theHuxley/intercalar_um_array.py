#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Voc� deve intercalar dois arrays de n�meros inteiros.

Formato de entrada
Na primeira linha voc� receber� um n�mero inteiro n indicando o tamanho de cada um dos arrays.
As pr�ximas n linhas correspondem aos elementos do primeiro array.
Depois seguir�o mais n linhas correspondendo aos elementos do segundo array.

Voc� deve imprimir 2n linhas com os arrays intercalados. Por exemplo, se a entrada for:
3
1
5
9
2
4
8
Voc� deve imprimir:
1
2
5
4
9
8
"""
count = int(input())
count2 = count
count = count * 2
num1 = []
num2 = []
while count > 0:
    if count <= count2:
        num2.append(int(input()))
    else:
        num1.append(int(input()))
    count -= 1
for i in range(count2):
    print(num1[i])
    print(num2[i])