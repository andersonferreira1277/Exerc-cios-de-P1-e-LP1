#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Em um torneio de futsal organizado todo semestre pela UFPB, o prêmio em dinheiro que os organizadores oferecem é dividido da seguinte maneira: 60 % para o vencedor, 30 % para o segundo colocado e 10 % para o terceiro. Escreva um programa que receba o valor total da premiação e exiba o valor pago a cada um dos três melhores colocados.

Formato de entrada
Um número real com duas casas decimais
Dica: não use mensagens no input

Formato de saída
Três números reais, cada um com duas casas decimais
Dica: Não use mensagens no print e lembre-se de formatar o número.
Exemplo: print("%.2f" %variavel) vai exibir a variável com duas casas decimais
"""
total = float(input())
print ("%.2f" % (total*0.60))
print ("%.2f" % (total*0.30))
print ("%.2f" % (total*0.10))