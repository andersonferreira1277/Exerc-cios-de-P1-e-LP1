#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Genival é ascensorista da Prefeitura Municipal e todos os dias conduz os passageiros para cima e para baixo. O elevador que ele opera tem capacidade para no máximo 7 pessoas e no máximo 560 quilos.
Escreva um programa que receba como entrada o peso de várias pessoas que estão entrando no elevador e exiba quantas poderão ser transportadas com segurança e o peso total carregado, respeitando os limites do elevador.

Formato de entrada
Vários valores reais
A entrada de dados será encerrada quando for informado o valor zero, ou quando um dos limites do elevador tiver sido atingido

Formato de saída
Um valor inteiro e um valor real com uma única casa decimal
"""
quilos = []
temp = 0
while True:
    temp = int(input())
    if temp == 0:
        break
    if (sum(quilos)+temp <= 560) and (len(quilos) < 7):
        quilos.append(temp)
    else:
        break
print len(quilos)
print ("%.1f" % (sum(quilos)))