#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Joaozinho quer calcular e mostrar a quantidade de litros de combust�vel gastos em uma viagem, ao utilizar um autom�vel que faz 12 KM/L. Para isso, ele gostaria que voc� o auxiliasse atrav�s de um simples programa. Para efetuar o c�lculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade m�dia durante a mesma (em km/h). Assim pode-se obter dist�ncia percorrida e em seguida calcular quantos litros seriam necess�rios. Mostre o valor com 3 casas decimais ap�s o ponto.

Formato de entrada
O arquivo de entrada cont�m dois inteiros. O primeiro � o tempo gasto na viagem (em horas) e o segundo � a velocidade m�dia durante a mesma (em km/h).

Formato de sa�da
Imprima a quantidade de litros necess�ria para realizar a viagem, com tr�s d�gitos ap�s o ponto decimal.
"""
def Litros(t,v):
    total = t*v
    return total/12
t = float(input())
v = float(input())
print ("%.3f" % Litros(t,v))
