#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o

A Organiza��o de Bocha Internacional � respons�vel por organizar a competi��o mundial de
bocha. Infelizmente esse esporte n�o � muito popular, e numa tentativa de aumentar a sua
popularidade, ficou decidido que seriam chamados, para a Grande Final Mundial, o campe�o
e o vice-campe�o de cada sede nacional, ao inv�s de apenas o primeiro lugar.

Tumb�lia � um pa�s pequeno que j� havia realizado a sua competi��o nacional quando a nova
regra foi institu�da, e o comit� local n�o armazenou quem foi o segundo classificado.
Felizmente eles armazenaram a pontua��o de todos competidores - que foram apenas tr�s,
devido ao tamanho diminuto do pa�s. Sabe-se tamb�m que as pontua��es de todos jogadores
foram diferentes, de forma que n�o ocorreu empate entre nenhum deles.
Resta agora descobrir quem foi o vice-campe�o e para isso o comit� precisa de ajuda.

Formato de entrada

A primeira e �nica linha da entrada consiste de tr�s inteiros separados por espa�os, A, B
e C, as pontua��es dos 3 competidores.
Considere:
1 <= A <= 100
1 <= B <= 100
1 <= C <= 100

Formato de sa�da

Imprima uma �nica linha na sa�da, contendo apenas um n�mero inteiro, a pontua��o do
vice-campe�o.
"""
num = []
num = map(int, raw_input().split())
num.sort()
print num[1]