#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Todo mundo provavelmente sabe que o jogo Zerinho ou um, usado para determinar um vencedor entre tr�s ou mais jogadores.
Para aqueles n�o familiarizados, o jogo funciona da seguinte maneira:
Cada jogador escolhe um valor entre zero ou um; solicitado por um comando (geralmente um dos competidores anuncia " Zerinho ou.... Um!")
Todos os participantes mostram uma m�o: se o valor escolhido � um, o competidor mostra uma m�o com um dedo estendido, se o valor escolhido for zero, o competidor mostra uma m�o com todos os dedos fechados. O ganhador � o �nico que optou por um valor diferente de todos os outros. Se n�o houver nenhum jogador com um valor de diferentes de todas as outras ( por exemplo, todos os jogadores escolhem zero, ou alguns jogadores escolhem zero e alguns jogadores escolheram um), n�o h� nenhum vencedor.
Alice, Bob e Clara s�o grandes amigos e jogam Zerinho ou Um o tempo todo, para determinar quem vai comprar a pipoca durante a sess�o de cinema, quem vai entrar na nata��o primeiro etc. Eles jogam tanto que eles decidiram fazer um plugin para jogar Zerinho ou Um no Facebook. Mas eles n�o sabem como programar, ent�o dividiram as tarefas entre os amigos que sabem, inclusive voc�.
Dadas os tr�s valores escolhidos por Alice, Bob e Clara, cada valor de zero ou um, escrever um programa que determina se h� um vencedor, e, nesse caso, determinar quem � o vencedor.

Formato de entrada
A entrada cont�m tr�s inteiros A, B e C (cada um pode ser 0 ou 1), indicando, respectivamente, os valores escolhidos por Alice, Beto e Clara.

Formato de sa�da
Seu programa deve imprimir uma linha, com um caracter em mai�sculo. Se Alice � o vencedor do personagem deve ser 'A', se Beto � o vencedor do personagem deve ser 'B', se Clara � o vencedor do personagem deve ser 'C', e se n�o houver vencedor o personagem deve ser '* '(asterisco).
No final, imprimir uma quebra de linha.
"""
a = int(input())
b = int(input())
c = int(input())
if (a == b) and (a == c):
    print ("*")
elif (a != b) and (a != c):
    print ("A")
elif (b != c) and (b != a):
    print ("B")
elif (c != b) and (c != a):
    print ("C")