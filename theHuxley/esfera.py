#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Fa�a um programa que calcule o mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A f�rmula para calcular o volume �: 4/3 * pi * R3. Considere (atribua) para pi o valor 3.14159.

Formato de entrada
O arquivo de entrada cont�m um valor inteiro, correspondente ao raio da esfera.

Formato de sa�da
A sa�da dever� ser uma mensagem "VOLUME" conforme o exemplo fornecido no caso de sa�da, com um espa�o antes e um espa�o depois da igualdade. O valor dever� ser apresentado com 3 casas ap�s o ponto.

http://mundoeducacao.bol.uol.com.br/matematica/volume-esfera.htm
"""
import math
a = int(input())
resultado = (4*math.pi*a**3)/3
print ("VOLUME = %.3F" % resultado)