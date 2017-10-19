#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. Escrever um programa para ler o ano em que a criança toma a 1a dose e a periodicidade (intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total.
A tabela abaixo traz exemplos de entrada e saída esperadas.

Formato de entrada
2016
4

Formato de saída
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