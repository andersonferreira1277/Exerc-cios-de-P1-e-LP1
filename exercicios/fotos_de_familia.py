#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Ambrosina é uma fotógrafa muito peculiar. Ela só aceita tirar fotos de pessoas se as pessoas estiverem em grupos de exatamente 04 pessoas. Tudo isso porque Ambrosina tem uma mania esquisita de ordenação. Para ela, a pessoa mais baixa deve ficar sempre do lado esquerdo, a segunda mais baixa do lado direito, no meio, logo após a mais baixa, fica a terceira mais baixa e em seguida a mais alta.
Abaixo segue uma ilustração de uma foto tirada por Ambrosina:

Formato de entrada
A entrada consiste de 04 números reais maiores que zero correspondendo às alturas de 04 pessoas. Cada número é dado em uma linha diferente. A entrada pode não estar ordenada.

Formato de saída
Consiste de 04 números reais, separados por um final de linha, ordenados de acordo com a mania de Ambrosina. Os números devem ser formatados com 02 casas decimais.
"""
num = []
num.append(float(input()))
num.append(float(input()))
num.append(float(input()))
num.append(float(input()))
num.sort()
print ("%.2f" % num[0])
print ("%.2f" % num[2])
print ("%.2f" % num[3])
print ("%.2f" % num[1])