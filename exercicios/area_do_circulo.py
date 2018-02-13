#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Guido é um cientista, ele foi chamado para resolver um problema da usina do senhor Ambrósio. Senhor Ambrósio quer construir uma usina de tratamento de água onde o aproveitamento do espaço seja o melhor possível. Ele lhe deu uma folha que contém o raio dos locais onde pretende fazer os tanques redondos.
Ele espera receber de Guido dados que contenham a área de cada tanque o qual lhe deu o raio.
Porém Guido está muito atarefado e pediu sua ajuda para fazer um programa que possa calcular a área de cada tanque de forma mais rápida.
Considerando que para este problema ? = 3.14159.
- Efetue o cálculo da área.

Formato de entrada
A entrada contém um valor de ponto flutuante que simboliza o raio.
Obs.: O raio é dado em cm.

Formato de saída
Apresentar a mensagem ?Area = ? seguido pelo valor da variável area dada em m², conforme exemplo de saída, com 4 casas após o ponto decimal. Você deve arredondar o valor. Não esqueça de imprimir o fim de linha após o resultado.
"""
import math
a = float(input())
pi = 3.14159
area = pi*a**2
area = round(area)
area = area/10000
print ("Area = %.4f\n" % area)