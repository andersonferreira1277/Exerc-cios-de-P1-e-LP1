#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Em um torneio de futsal organizado todo semestre pela UFPB, o pr�mio em dinheiro que os organizadores oferecem � dividido da seguinte maneira: 60 % para o vencedor, 30 % para o segundo colocado e 10 % para o terceiro. Escreva um programa que receba o valor total da premia��o e exiba o valor pago a cada um dos tr�s melhores colocados.

Formato de entrada
Um n�mero real com duas casas decimais
Dica: n�o use mensagens no input

Formato de sa�da
Tr�s n�meros reais, cada um com duas casas decimais
Dica: N�o use mensagens no print e lembre-se de formatar o n�mero.
Exemplo: print("%.2f" %variavel) vai exibir a vari�vel com duas casas decimais
"""
total = float(input())
print ("%.2f" % (total*0.60))
print ("%.2f" % (total*0.30))
print ("%.2f" % (total*0.10))