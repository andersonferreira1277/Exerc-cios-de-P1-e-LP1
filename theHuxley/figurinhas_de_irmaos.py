#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Jo�o e Maria s�o dois irm�os muito briguentos. Um belo dia, o pai deles, o Sr. Carlos, comprou v�rias figurinhas do �lbum da copa. Jo�o disse que por ser menino tinha direito a mais figurinhas. Obviamente, Maria n�o concordou e prop�s um acordo de risco. Eles iriam dividir as figurinhas da seguinte maneira:
Jo�o ficaria com todas as figurinhas cujo n�mero de s�rie for par e Maria com as �mpares. O Sr. Carlos gostou da id�ia e prop�s um pequeno b�nus:
- Aquele que obtivesse o maior valor somando os n�meros de s�ries das figurinhas ganharia como b�nus mais R$10,00 reais para comprar figurinhas s� para ele.

Formato de entrada
Consiste de um n�mero inteiro n indicando a quantidade de figurinhas a serem lidas, seguido de n inteiros correspondendo ao n�mero de s�rie de cada
figurinha. Todas as figurinhas possuem n�meros de s�rie diferentes. Note que as figurinhas podem ser repetidas. Neste caso, s� devemos considerar na soma do n�mero de s�rie uma �nica vez, mas contamos na quantidade de figurinhas.
Considere:
 n <= 10.000
Cada inteiro <= 10.000

Formato de sa�da
Consiste dos n�meros inteiros J, M e S, indicando respectivamente, o n�mero de figurinhas que ficaram com o Jo�o, o n�mero de figurinhas que ficaram com Maria e a soma dos n�meros de s�rie do irm�o que ganhou o b�nus do Sr. Carlos.
Depois de cada n�mero da sa�da coloque um final de linha.
"""
count = int(input())
menino = []
menina = []
menino_soma = []
menina_soma = []
while count > 0:
     entrada = int(input())
     if entrada%2 == 0:
         menino.append(entrada)
         if entrada in menino_soma:
             menino_soma = menino_soma # essa linha n�o faz nada, mas break termina todo o loop while, antes de terminar a entrada
         else:
             menino_soma.append(entrada)
     elif entrada%2 != 0:
         menina.append(entrada)
         if entrada in menina_soma:
             menina_soma = menina_soma # essa linha n�o faz nada, mas break termina todo o loop while, antes de terminar a entrada
         else:
             menina_soma.append(entrada)
     count -= 1
print(len(menino))
print(len(menina))
menino_soma = sum(menino_soma)
menina_soma = sum(menina_soma)
if menino_soma > menina_soma:
    print(menino_soma)
elif menina_soma > menino_soma:
    print(menina_soma)