#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Genival � ascensorista da Prefeitura Municipal e todos os dias conduz os passageiros para cima e para baixo. O elevador que ele opera tem capacidade para no m�ximo 7 pessoas e no m�ximo 560 quilos.
Escreva um programa que receba como entrada o peso de v�rias pessoas que est�o entrando no elevador e exiba quantas poder�o ser transportadas com seguran�a e o peso total carregado, respeitando os limites do elevador.

Formato de entrada
V�rios valores reais
A entrada de dados ser� encerrada quando for informado o valor zero, ou quando um dos limites do elevador tiver sido atingido

Formato de sa�da
Um valor inteiro e um valor real com uma �nica casa decimal
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