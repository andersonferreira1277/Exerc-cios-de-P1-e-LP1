#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Periodicamente as crian�as brasileiras devem tomar vacinas que as protegem de diversas doen�as. Escrever um programa para ler o ano em que a crian�a toma a 1a dose e a periodicidade (intervalo em anos) da vacina e exibir em que outros anos a crian�a deve tomar as pr�ximas doses desta vacina, sabendo que s�o 4(quatro) doses ao total.
A tabela abaixo traz exemplos de entrada e sa�da esperadas.

Formato de entrada
2016
4

Formato de sa�da
2020 2024 2028
"""
ano = int(input())
periodo = int(input())
resultado = []
count = 4
while count > 1:
    resultado.append(ano+periodo)
    ano = ano+periodo
    count -= 1
print ("%d %d %d" % (resultado[0],resultado[1],resultado[2]))