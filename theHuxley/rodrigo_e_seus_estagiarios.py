#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Rodrigo � um professor rigoroso. Ele sempre d� muitos afazeres aos seus estagi�rios. Ent�o seus estagi�rios decidiram matar ele. Vai haver uma festa de comemora��o na sede do huxley s�bado � noite , e seus estagi�rios decidiram matar ele no mesmo dia.
Na festa existem N garrafas de coca-cola. Cada garrafa cont�m um X escrito nela, os estagi�rios decidiram misturar veneno em algumas delas. Eles fizeram um plano para adicionar veneno somente nas garrafas que cont�m um inteiro tal que esse inteiro tenha o n�mero de divisores estritamente menor que 4.
De alguma forma o professor rodrigo descobriu o plano e pediu a sua ajuda para saber de quais garrafas ele pode beber.

Formato de entrada

A primeira linha cont�m um inteiro N indicando a quantidade de testes.
Cada teste cont�m um n�mero X indicando o inteiro escrito na garrafa.
1 <= N <= 105
1 <= X <= 107

Formato de sa�da
Para cada garrafa imprima YES caso rodrigo possa beber a garrafa e  NO caso ela esteja envenenada.
"""
from math import ceil
limite = long(input())
if limite <= 10**5 and limite>= 1:
    count = 1
    lista = []
    while count <= limite:
        temp = long(input())
        if temp <= 10**7 and temp >= 1:
            lista.append(temp)
        count += 1
    for i in lista:
        if i % 2 == 0:
            if i == 2 or i == 4:
                print ("NO")
            else:
                print ("YES")
        else:
            divisores = 0
            for x in range(1,int(ceil(i*0.5+1))):
                divisores = divisores + 1 if i % x == 0 else divisores
                if divisores > 3:
                    break
            if divisores < 4:
                print ("NO")
            else:
                print ("YES")