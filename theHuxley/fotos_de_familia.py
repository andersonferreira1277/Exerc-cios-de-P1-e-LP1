#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Ambrosina � uma fot�grafa muito peculiar. Ela s� aceita tirar fotos de pessoas se as pessoas estiverem em grupos de exatamente 04 pessoas. Tudo isso porque Ambrosina tem uma mania esquisita de ordena��o. Para ela, a pessoa mais baixa deve ficar sempre do lado esquerdo, a segunda mais baixa do lado direito, no meio, logo ap�s a mais baixa, fica a terceira mais baixa e em seguida a mais alta.
Abaixo segue uma ilustra��o de uma foto tirada por Ambrosina:

Formato de entrada
A entrada consiste de 04 n�meros reais maiores que zero correspondendo �s alturas de 04 pessoas. Cada n�mero � dado em uma linha diferente. A entrada pode n�o estar ordenada.

Formato de sa�da
Consiste de 04 n�meros reais, separados por um final de linha, ordenados de acordo com a mania de Ambrosina. Os n�meros devem ser formatados com 02 casas decimais.
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