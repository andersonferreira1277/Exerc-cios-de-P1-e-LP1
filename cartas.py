#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Beatriz gosta muito de jogar cartas com as amigas. Para treinar mem�ria e racioc�nio l�gico, ela inventou um pequeno passatempo com cartas. Ela retira as cinco primeiras cartas do topo de um baralho bem embaralhado, e as coloca em sequ�ncia, da esquerda para a direita, na mesa, com as faces voltadas para baixo.
Ent�o ela olha, por um breve instante, cada uma das cartas da sequ�ncia (e logo as recoloca na mesa, com a face para baixo). Usando apenas a sua mem�ria, Beatriz deve agora dizer se a sequ�ncia de cartas est� ordenada crescentemente, decrescentemente, ou n�o est� ordenada.
De tanto jogar, ela est� ?cando cansada, e n�o con?a em seu pr�prio julgamento para saber se acertou ou errou. Por isso, ela pediu para voc� fazer um programa que, dada uma sequ�ncia de cinco cartas, determine se a sequ�ncia dada est� ordenada crescentemente, decrescentemente, ou n�o est� ordenada.

Formato de entrada
A entrada consiste de uma �nica linha que cont�m as cinco cartas da sequ�ncia. Os valores das cartas s�o representados por inteiros entre 1 e 13. As cinco cartas t�m valores distintos.

Formato de sa�da
Seu programa deve produzir uma �nica linha, contendo um �nico caractere mai�sculo: ?C? caso a sequ�ncia dada esteja ordenada crescentemente, ?D? se estiver ordenada decrescentemente, ou ?N? caso contr�rio.
N�o coloque nenhum final de linha depois do caractere.
"""
lista = map(int, raw_input().split())
crescente = []
decrescente = []
for i in lista:
    crescente.append(i)
crescente.sort()
for i in lista:
    decrescente.append(i)
decrescente.sort(reverse=True)
if lista == crescente:
    print ("C")
elif lista == decrescente:
    print ("D")
else:
    print ("N")