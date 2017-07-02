#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Beatriz gosta muito de jogar cartas com as amigas. Para treinar memória e raciocínio lógico, ela inventou um pequeno passatempo com cartas. Ela retira as cinco primeiras cartas do topo de um baralho bem embaralhado, e as coloca em sequência, da esquerda para a direita, na mesa, com as faces voltadas para baixo.
Então ela olha, por um breve instante, cada uma das cartas da sequência (e logo as recoloca na mesa, com a face para baixo). Usando apenas a sua memória, Beatriz deve agora dizer se a sequência de cartas está ordenada crescentemente, decrescentemente, ou não está ordenada.
De tanto jogar, ela está ?cando cansada, e não con?a em seu próprio julgamento para saber se acertou ou errou. Por isso, ela pediu para você fazer um programa que, dada uma sequência de cinco cartas, determine se a sequência dada está ordenada crescentemente, decrescentemente, ou não está ordenada.

Formato de entrada
A entrada consiste de uma única linha que contém as cinco cartas da sequência. Os valores das cartas são representados por inteiros entre 1 e 13. As cinco cartas têm valores distintos.

Formato de saída
Seu programa deve produzir uma única linha, contendo um único caractere maiúsculo: ?C? caso a sequência dada esteja ordenada crescentemente, ?D? se estiver ordenada decrescentemente, ou ?N? caso contrário.
Não coloque nenhum final de linha depois do caractere.
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