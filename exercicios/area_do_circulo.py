#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Guido � um cientista, ele foi chamado para resolver um problema da usina do senhor Ambr�sio. Senhor Ambr�sio quer construir uma usina de tratamento de �gua onde o aproveitamento do espa�o seja o melhor poss�vel. Ele lhe deu uma folha que cont�m o raio dos locais onde pretende fazer os tanques redondos.
Ele espera receber de Guido dados que contenham a �rea de cada tanque o qual lhe deu o raio.
Por�m Guido est� muito atarefado e pediu sua ajuda para fazer um programa que possa calcular a �rea de cada tanque de forma mais r�pida.
Considerando que para este problema ? = 3.14159.
- Efetue o c�lculo da �rea.

Formato de entrada
A entrada cont�m um valor de ponto flutuante que simboliza o raio.
Obs.: O raio � dado em cm.

Formato de sa�da
Apresentar a mensagem ?Area = ? seguido pelo valor da vari�vel area dada em m�, conforme exemplo de sa�da, com 4 casas ap�s o ponto decimal. Voc� deve arredondar o valor. N�o esque�a de imprimir o fim de linha ap�s o resultado.
"""
import math
a = float(input())
pi = 3.14159
area = pi*a**2
area = round(area)
area = area/10000
print ("Area = %.4f\n" % area)