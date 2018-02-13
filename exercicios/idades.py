#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Escrever um algoritmo para ler um número indeterminado de dados, cada um contendo a idade de um indivíduo. O último número dado não deverá entrar nos cálculos e contém o valor de uma idade negativa.
Calcule e imprima a idade média deste grupo de indivíduos.

Formato de entrada
A entrada contém um número indeterminado de números inteiros. A entrada irá parar quando um valor negativo é lido.

Formato de saída
A saída contém um valor correspondente para a idade média dos indivíduos.
A média deve ser impresso com duas casas decimais, seguido de uma quebra de linha.
"""
idades = []
while True:
    temp = float(input())
    if temp >= 0:
        idades.append(temp)
    else:
        break
print ("%.2f" % ((sum(idades))/len(idades)))