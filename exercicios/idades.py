#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Escrever um algoritmo para ler um n�mero indeterminado de dados, cada um contendo a idade de um indiv�duo. O �ltimo n�mero dado n�o dever� entrar nos c�lculos e cont�m o valor de uma idade negativa.
Calcule e imprima a idade m�dia deste grupo de indiv�duos.

Formato de entrada
A entrada cont�m um n�mero indeterminado de n�meros inteiros. A entrada ir� parar quando um valor negativo � lido.

Formato de sa�da
A sa�da cont�m um valor correspondente para a idade m�dia dos indiv�duos.
A m�dia deve ser impresso com duas casas decimais, seguido de uma quebra de linha.
"""
idades = []
while True:
    temp = float(input())
    if temp >= 0:
        idades.append(temp)
    else:
        break
print ("%.2f" % ((sum(idades))/len(idades)))