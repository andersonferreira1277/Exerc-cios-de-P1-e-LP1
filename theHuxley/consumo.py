#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Calcule o consumo m�dio de um autom�vel sendo fornecidos a dist�ncia total percorrida (em Km) e o total de combust�vel gasto (em litros).

Formato de entrada
O arquivo de entrada cont�m dois valores: um valor inteiro X representando a dist�ncia total percorrida (em Km) e um valor real Y representando o total de combust�vel gasto.

Formato de sa�da
Apresente o valor que representa o consumo m�dio do autom�vel com 3 casas ap�s a v�rgula, seguido da mensagem "km/l".
"""
a = float(input())
b = float(input())
resultado = a/b
print ("%.3f km/l" % resultado)