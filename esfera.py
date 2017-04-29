#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Faça um programa que calcule o mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: 4/3 * pi * R3. Considere (atribua) para pi o valor 3.14159.

Formato de entrada
O arquivo de entrada contém um valor inteiro, correspondente ao raio da esfera.

Formato de saída
A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido no caso de saída, com um espaço antes e um espaço depois da igualdade. O valor deverá ser apresentado com 3 casas após o ponto.

http://mundoeducacao.bol.uol.com.br/matematica/volume-esfera.htm
"""
import math
a = int(input())
resultado = (4*math.pi*a**3)/3
print ("VOLUME = %.3F" % resultado)