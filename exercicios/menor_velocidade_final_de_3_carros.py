# -*- coding: latin1 -*-
# windows 10 64 bits
# python 2.7.12
# Feito por andersonferreira1277@gmail.com
"""
Descrição
Escreva uma função chamada velkmh que calcule a velocidade final (em km/h) de um automóvel a partir dos valores da velocidade inicial V0 (em m/s), da aceleração A (em m/s2 - metros por segundo ao quadrado) e do tempo de percurso T (em s) passados como parâmetro.
Escreva um programa que faça uso dessa função para comparar o valor da velocidade final de três automóveis e exiba o menor dos três valores como resultado.
Fórmulas de referência para o problema:
V = V0 + A*T
Vkm/h = 3.6 * Vm/s

Formato de entrada
A entrada para este programa constará de valores de V0, A e T (nesta ordem) para cada um dos três automóveis.

Formato de saída
A saída deve ser o menor valor de V em km/h calculado. Utilize uma casa decimal para a velocidade a ser impressa como resultado.
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