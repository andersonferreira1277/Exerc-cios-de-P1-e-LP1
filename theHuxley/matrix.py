#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Em um futuro pr�ximo, voc�, um(a) jovem programador(a) de computador mora em um cub�culo escuro e � atormentado(a) por estranhos pesadelos nos quais encontra-se conectado por cabos contra sua vontade, em um imenso sistema de computadores do futuro. Esse repetido pesadelo faz com que voc� comece a ter d�vidas sobre a realidade.
Certa noite voc� encontrou um panfleto pr�ximo a um orelh�o que dizia:

wake up? the matrix has you?
Sei por que mal dorme, porque mora sozinho e porque, noite ap�s noite, senta-se ao computador. Voc� est� procurando...
Voc� sentiu a vida inteira que h� alguma coisa errada com o mundo, voc� n�o sabe o que �, mas est� ali como uma farpa em sua mente, deixando-o louco(a)
Para saber a verdade voc� precisa passar no teste:

V� at� o orelh�o responda as seguintes perguntas com ?1? para ?SIM? e ?0? para ?N�O?:

1.Voc� acredita em destino?
2.Voc� sentiu a vida inteira que h� algo errado com o mundo?
3.Voc� j� teve um sonho que parecesse realidade?
4.Voc� quer saber a verdade?
5.Voc� quer saber o que � Matrix?

Fa�a um programa para calcular os pontos, onde:
Para a 1� pergunta se a resposta for 0, ou seja ?n�o?, ganha 2 pontos.
Para a 2�, 3� e 4�  pergunta se a resposta for 1, ou seja ?sim?, ganha 1 pontos.
Para a 5� pergunta se a resposta for 1, ou seja ?sim?, ganha 3 pontos.
Se o total de pontos for maior ou igual a 5 imprima:
?A Matrix esta em todo lugar. A nossa volta. E o mundo colocado diante de seus olhos, para que nao veja a verdade. Infelizmente a impossivel dizer o que a a Matrix. Voc� tem de ver por si mesmo. *Voce a sugado pelo telefone e revelado a verdade ?*?
Se o total de pontos for menor que 5 imprima:
?Voce precisa entender que a maioria dessas pessoas nao estao prontas para acordar. E muitos estao tao inertes, tao dependentes do sistema que vao lutar para protege-lo.?
"""
nota = 0
a = bool(input())
if a == False:
    nota += 2
b = bool(input())
if b == True:
    nota += 1
c = bool(input())
if c == True:
    nota += 1
d = bool(input())
if d == True:
    nota += 1
f = bool(input())
if f == True:
    nota += 3
if nota >= 5:
    print ("A Matrix esta em todo lugar. A nossa volta. E o mundo colocado diante de seus olhos, para que nao veja a verdade. Infelizmente e impossivel dizer o que e a Matrix. Voce tem de ver por si mesmo. *Voce e sugado pelo telefone e revelado a verdade")
else:
    print ("Voce precisa entender que a maioria dessas pessoas nao estao prontas para acordar. E muitos estao tao inertes, tao dependentes do sistema que vao lutar para protege-lo")