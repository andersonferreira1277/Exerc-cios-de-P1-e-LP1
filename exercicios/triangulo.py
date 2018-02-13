#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Os tri�ngulos mais simples s�o classificados de acordo com os limites das propor��es relativas de seus lados:
Um tri�ngulo equil�tero possui todos os lados congruentes ou seja iguais. Um tri�ngulo equil�tero � tamb�m equi�ngulo: todos os seus �ngulos internos s�o congruentes (medem 60�), sendo, portanto, classificado como um pol�gono
regular.
Um tri�ngulo is�sceles possui pelo menos dois lados de mesma medida e dois �ngulos congruentes. O tri�ngulo equil�tero �, conseq�entemente,
um caso especial de um tri�ngulo is�sceles, que apresenta n�o somente dois, mas todos os tr�s lados iguais, assim como os �ngulos, que medem
todos 60�. Num tri�ngulo is�sceles, o �ngulo formado pelos lados congruentes � chamado �ngulo do v�rtice. Os demais �ngulos
denominam-se �ngulos da base e s�o congruentes.
Em um tri�ngulo escaleno, as medidas dos tr�s lados s�o diferentes. Os �ngulos internos de um tri�ngulo escaleno tamb�m possuem medidas
diferentes.
Sua miss�o � escrever um programa para classificar um tri�ngulo de lados de comprimentos dados em: escaleno (os tr�s lados de comprimentos diferentes), is�sceles (dois lados de comprimentos iguais) ou equil�tero (os tr�s lados de comprimentos iguais).

Formato de entrada
A entrada consiste de 03 n�meros reais maiores que zero correspondendo ao comprimento dos lados do tri�ngulo.

Formato de sa�da
A sa�da deve ser: "escaleno", "isosceles" ou "equilatero" seguido de um final delinha.
Obs.: as aspas acima n�o devem ser impressas e a sa�da deve ser impressa sem acentos.
"""
# entrada
a = int(input())
b = int(input())
c = int(input())

if (a == b) and (a == c):
    print("equilatero")
elif (a == b) or (a == c) or (b == c):
    print("isosceles")
else:
    print("escaleno")