#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Rodrigo é um professor rigoroso. Ele sempre dá muitos afazeres aos seus estagiários. Então seus estagiários decidiram matar ele. Vai haver uma festa de comemoração na sede do huxley sábado à noite , e seus estagiários decidiram matar ele no mesmo dia.
Na festa existem N garrafas de coca-cola. Cada garrafa contém um X escrito nela, os estagiários decidiram misturar veneno em algumas delas. Eles fizeram um plano para adicionar veneno somente nas garrafas que contém um inteiro tal que esse inteiro tenha o número de divisores estritamente menor que 4.
De alguma forma o professor rodrigo descobriu o plano e pediu a sua ajuda para saber de quais garrafas ele pode beber.

Formato de entrada

A primeira linha contém um inteiro N indicando a quantidade de testes.
Cada teste contém um número X indicando o inteiro escrito na garrafa.
1 <= N <= 105
1 <= X <= 107

Formato de saída
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