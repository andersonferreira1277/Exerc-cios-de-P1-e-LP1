#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
As quatro estações do ano variam de acordo com as datas:
Primavera: 21 setembro até 20 dezembro
Verão: 21 dezembro até 20 março
Outono: 21 março até 20 junho
Inverno: 21 junho até 20 setembro
Escreva uma função chamada EstacaoAno que receba como entrada um dia e um mês e retorne o nome da estação correspondente.

Formato de entrada
Dois valores inteiros, representando o dia e o mês nessa sequência

Formato de saída
Um String em letras maiúsculas
Obs: Não use acento em VERAO
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