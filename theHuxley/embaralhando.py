# -*- coding: latin1 -*-
# windows 10 64 bits
# python 2.7.12
# Feito por andersonferreira1277@gmail.com
"""
Descri��o
Gabriel � aluno do curso de ci�ncia da computa��o, ele sempre gostou de jogos de l�gica, um exemplo � o cubo m�gico, os alunos ficam admirados em ver a facilidade que ele tem para resolv�-lo. Gabriel decidiu montar seu pr�prio jogo envolvendo l�gica, a primeira informa��o que ele ir� precisar para montar o jogo � de quantos anagramas � poss�vel formar com certa quantidade de caracteres distintos sem espa�o.
Como ele tem se dedicado muito para maratona de programa��o, ele acaba n�o tendo tempo para verificar isso, por isso precisar� de sua ajuda.
Sua tarefa �, dado um conjunto de caracteres distintos e sem espa�os, informar quantos anagramas � poss�vel formar.

Formato de entrada
A entrada � composta por v�rios casos de teste. Cada caso de teste ter� uma �nica linha S com no m�ximo 15 caracteres. A entrada termina quando S = 0 e n�o deve ser processada.

Formato de sa�da
Para cada caso de teste voc� dever� imprimir quantos anagramas s�o poss�veis formar com os caracteres informados.
"""
palavras = []
while True:
    temp = raw_input()
    if temp == "0":
        break
    palavras.append(temp)
for i in palavras:
    i = len(i)
    resultado = 1
    for x in range(i,1,-1):
        resultado = resultado*x
    print resultado