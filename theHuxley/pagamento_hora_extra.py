#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Sam � diretor na empresa XYZ e um de seus projetos est� atrasado. Para conseguir conclu�-lo no tempo estimado, ele decidiu pagar a cada funcion�rio 5% de seu sal�rio por cada hora extra trabalhada. Crie um programa que receba como entrada o sal�rio de um funcion�rio e a quantidade de horas extras que ele trabalhou, calcule e exiba o valor total que dever� ser pago a ele.

Formato de entrada

Um n�mero real com duas casas decimais representando o sal�rio.
Um n�mero inteiro representando as horas extras.
Dica: n�o use mensagens no input.

Formato de sa�da
Um n�mero real com duas casas decimais
Dica: N�o use mensagens no print e lembre-se de formatar o n�mero.
Exemplo: print("%.2f" %variavel) vai exibir a vari�vel com duas casas decimais.
"""
salario = float(input())
horas = int(input())
print ("%.2f" % ((salario*0.05)*horas+salario))