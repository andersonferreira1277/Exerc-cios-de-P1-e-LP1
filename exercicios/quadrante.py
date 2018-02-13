#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Escreva um programa para ler as coordenadas (X, Y) de um ponto no sistema cartesiano. E escrever à qual quadrante ele pertence.

Formato de entrada
Dois números inteiros.

Formato de saída
Imprima o quadrante correspondente que estas coordenadas pertencem, que pode ser:
primeiro
segundo
terceiro
quarto
eixo x
eixo y
origem
Será eixo x quando a coordenada y for zero.
Será eixo y quando a coordenada x for zero.
Os outros basta achar a localização do ponto no plano cartesiano.
A saida deve ser seguida de uma quebra de linha.
"""
#===============================entrada=============================================
a = raw_input()
x, y = a.split()
x = int(x)
y = int(y)
#===================================================================================
if (x == 0) and (y == 0):
    print("origem")
elif (y == 0) and (x != 0):
    print("eixo x")
elif (x == 0) and (y != 0):
    print("eixo y")
elif (x > 0) and (y > 0):
    print("primeiro")
elif (x > 0) and (y < 0):
    print("quarto")
elif (x < 0) and (y > 0):
    print("segundo")
elif (x < 0) and (y < 0):
    print("terceiro")