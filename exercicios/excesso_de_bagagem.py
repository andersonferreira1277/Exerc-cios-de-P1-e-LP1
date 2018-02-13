#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
A companhia a�rea Fly Fast tem rigorosas regras para as bagagens conduzidas por seus passageiros. O limite aceit�vel � de 20 kg, e bagagens acima disso s�o taxadas:
Peso
Regra
At� 20 kg
Nenhuma taxa � cobrada
Entre 21 kg e 25 kg
Cobran�a de taxa de R$ 12,50 por peso adicional
Entre 26 kg e 30 kg
Cobran�a de taxa de R$ 32,75 por peso adicional
Acima de 30 kg
Peso n�o permitido pela empresa
Escreva um programa que receba como entrada o peso da bagagem de um cliente e exiba o valor da taxa a ser paga, ou uma mensagem informando que o peso limite foi excedido.

Formato de entrada
Um valor real

Formato de sa�da
Um valor real OU a mensagem PESO LIMITE EXCEDIDO
Obs: a mensagem exibida n�o pode diferente dessa e deve estar toda em mai�sculas
"""
a = float(input())
#condi��es
if a <= 20:
    print("0.00")
elif (a > 20) and (a <= 25):
    total = (a-20) * 12.50
    print("%.2f" % total)
elif (a > 25) and a <= 30:
    total = (a - 20) * 32.75
    print("%.2f" % total)
elif a > 30:
    print("PESO LIMITE EXCEDIDO")