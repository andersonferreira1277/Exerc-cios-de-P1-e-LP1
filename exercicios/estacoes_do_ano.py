#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
As quatro esta��es do ano variam de acordo com as datas:
Primavera: 21 setembro at� 20 dezembro
Ver�o: 21 dezembro at� 20 mar�o
Outono: 21 mar�o at� 20 junho
Inverno: 21 junho at� 20 setembro
Escreva uma fun��o chamada EstacaoAno que receba como entrada um dia e um m�s e retorne o nome da esta��o correspondente.

Formato de entrada
Dois valores inteiros, representando o dia e o m�s nessa sequ�ncia

Formato de sa�da
Um String em letras mai�sculas
Obs: N�o use acento em VERAO
"""
def estacaoano(d,m):
    if m >=9 and m <=12:
        if (m == 12 and d <=20) or (m == 9 and d >=21) or (m > 9 and m < 12):
            return "PRIMAVERA"
    else:
        return "teste"
dia = int(input())
mes = int(input())
print estacaoano(dia,mes)