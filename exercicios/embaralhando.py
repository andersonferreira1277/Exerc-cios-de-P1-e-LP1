# -*- coding: latin1 -*-
# windows 10 64 bits
# python 2.7.12
# Feito por andersonferreira1277@gmail.com
"""
Descrição
Gabriel é aluno do curso de ciência da computação, ele sempre gostou de jogos de lógica, um exemplo é o cubo mágico, os alunos ficam admirados em ver a facilidade que ele tem para resolvê-lo. Gabriel decidiu montar seu próprio jogo envolvendo lógica, a primeira informação que ele irá precisar para montar o jogo é de quantos anagramas é possível formar com certa quantidade de caracteres distintos sem espaço.
Como ele tem se dedicado muito para maratona de programação, ele acaba não tendo tempo para verificar isso, por isso precisará de sua ajuda.
Sua tarefa é, dado um conjunto de caracteres distintos e sem espaços, informar quantos anagramas é possível formar.

Formato de entrada
A entrada é composta por vários casos de teste. Cada caso de teste terá uma única linha S com no máximo 15 caracteres. A entrada termina quando S = 0 e não deve ser processada.

Formato de saída
Para cada caso de teste você deverá imprimir quantos anagramas são possíveis formar com os caracteres informados.
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