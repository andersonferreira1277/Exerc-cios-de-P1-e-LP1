#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Leonardo � um corredor profissional que participa de diversos campeonatos de atletismo
pelo mundo. O tamanho das pistas ao redor do mundo n�o � padronizado. Por isso,
Leonardo, que treina em um clube que possui uma pista circular, resolveu fixar seu
treinamento em C metros, ao inv�s de um n�mero fixo de voltas na pista. Ap�s cada
treinamento, Leonardo deve tomar meio litro de �gua antes de fazer qualquer esfor�o,
e por isso quer deixar sua garrafa de �gua exatamente no ponto da pista onde ele
termina o seu treinamento.
Sabendo o comprimento da pista de corrida que Leonardo pretende treinar, ele resolveu
pedir sua ajuda para calcular o local do ponto de t�rmino do treinamento. O ponto de
t�rmino � o local da pista onde ele termina o percurso de C metros considerando que
ele parte do ponto de partida e se movimenta sempre na mesma dire��o. O ponto de
t�rmino � dado pelo n�mero de metros entre o ponto de partida e o local onde
Leonardo termina seu treinamento, contados na dire��o do percurso. Leonardo quer
deixar sua garrafa de �gua neste ponto.
Por exemplo, se a pista tem 12 metros e Leonardo fixou seu treinamento em 22 metros,
o ponto de t�rmino � 10.
Sua tarefa �, dado o n�mero C de metros que Leonardo pretende correr e o comprimento
N em metros da pista circular, determinar o ponto de t�rmino de seu treinamento.
"""
cn = raw_input()
cn = cn.split()
cn = map(int, cn)
print (cn[0]%cn[1])