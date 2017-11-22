#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior do que ou igual às duas prestações; estas devem ser iguais, inteiras e as maiores possíveis. Por exemplo, se o valor da mercadoria for R$ 270,00, a entrada e as duas prestações são iguais a R$ 90,00; se o valor da mercadoria for R$ 302,75, a entrada é de R$ 102,75 e as duas prestações são a iguais a R$ 100,00.
Escreva um programa que receba o valor da mercadoria e forneça o valor da entrada e das duas prestações, de acordo com as regras acima. A saída deve ser os 3 valores, linha a linha, em ponto flutuante com duas casas decimais de precisão.

Formato de entrada
Um valor N representando o valor da mercadoria.

Formato de saída
3 valores linha à linha, onde o primeiro é a entrada, e os demais as prestações.
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