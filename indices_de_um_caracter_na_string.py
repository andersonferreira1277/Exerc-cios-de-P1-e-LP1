#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o

Fa�a um progrma para ler uma string e um caracter qualquer e imprima as posi��es (�ndices) de onde ocorre o caracter na string. Por exemplo, seja a string "abracadabra!!!" e o caracter 'a', ent�o a sua sa�da deve ser:

0
3
5
7
10
-1
O valor -1 indica o final, ou seja, n�o existem mais ocorr�ncias. Caso n�o exista nenhuma ocorr�ncia, deve ser impresso o valor -1.
Considere tamb�m que o 0 representa o �ndice do primeiro caracter em uma string.

Formato de entrada
Voc� receber� duas linhas. A primeira linha cont�m a string e a segunda linha cont�m um caracter. O tamanho m�ximo da string � 50.

Formato de sa�da
Imprima os �ndices, sendo um por linha.
"""
a = raw_input()
b = raw_input()
indice = 0
count = 0
for i in a:
    if i == b:
        print indice
    indice += 1
print -1