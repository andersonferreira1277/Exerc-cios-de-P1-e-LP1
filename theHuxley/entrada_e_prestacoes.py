#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Uma loja vende seus produtos no sistema entrada mais duas presta��es, sendo a entrada maior do que ou igual �s duas presta��es; estas devem ser iguais, inteiras e as maiores poss�veis. Por exemplo, se o valor da mercadoria for R$ 270,00, a entrada e as duas presta��es s�o iguais a R$ 90,00; se o valor da mercadoria for R$ 302,75, a entrada � de R$ 102,75 e as duas presta��es s�o a iguais a R$ 100,00.
Escreva um programa que receba o valor da mercadoria e forne�a o valor da entrada e das duas presta��es, de acordo com as regras acima. A sa�da deve ser os 3 valores, linha a linha, em ponto flutuante com duas casas decimais de precis�o.

Formato de entrada
Um valor N representando o valor da mercadoria.

Formato de sa�da
3 valores linha � linha, onde o primeiro � a entrada, e os demais as presta��es.
"""
valor = float(input())
entrada = int
prestacao = int
decimal = valor - int(valor)
if int(valor) % 3 == 0 and decimal % 3 == 0:
    entrada = valor/3
    prestacao = valor/3
else:
    entrada = int((valor/3))+(valor%3)
    prestacao = int(valor/3)
print ("%.2f" % entrada)
print ("%.2f" % prestacao)
print ("%.2f" % prestacao)