# -*- coding: latin1 -*-
# windows 10 64 bits
# python 2.7.12
# Feito por andersonferreira1277@gmail.com
"""
Descri��o
Escreva uma fun��o chamada velkmh que calcule a velocidade final (em km/h) de um autom�vel a partir dos valores da velocidade inicial V0 (em m/s), da acelera��o A (em m/s2 - metros por segundo ao quadrado) e do tempo de percurso T (em s) passados como par�metro.
Escreva um programa que fa�a uso dessa fun��o para comparar o valor da velocidade final de tr�s autom�veis e exiba o menor dos tr�s valores como resultado.
F�rmulas de refer�ncia para o problema:
V = V0 + A*T
Vkm/h = 3.6 * Vm/s

Formato de entrada
A entrada para este programa constar� de valores de V0, A e T (nesta ordem) para cada um dos tr�s autom�veis.

Formato de sa�da
A sa�da deve ser o menor valor de V em km/h calculado. Utilize uma casa decimal para a velocidade a ser impressa como resultado.
"""
def velkmh(v,a,t):
    ms = v+a*t
    return ms*3.6

count = 1
menor_velocidade = float
lista = []
while count <= 3:
    v = float(input())
    a = float(input())
    t = float(input())
    lista.append(velkmh(v,a,t))
    count += 1
menor_velocidade = min(lista)
print ("%.1f" % menor_velocidade)