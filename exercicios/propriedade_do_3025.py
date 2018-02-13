#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Repare a seguinte característica do número 3025:
30 + 25 = 55 e 55^2 = 3025
Faça um programa que leia uma série de valores (números inteiros de 4 dígitos, um de cada vez) e diga se possuem a mesma característica. O programa termina quando for lido um valor menor que 1000 ou maior que 9999.

Formato de entrada
Uma sequência de números inteiros, separados por um final de linha

Formato de saída
Para cada número lido, seu programa deve imprimir:
"propriedade do 3025!", caso o número lido atenda à propriedade descrita acima, ou "numero comum" caso contrário.
Imprima um final de linha após cada saída.
obs: Sem as aspas.
"""
#===================entrada================================
num = []
count = int(input())
while count>=1000 and count<=9999:
    if count>=1000 and count<=9999:
        num.append(count)
    count = int(input())
#===========================================================
for i in num:
    x, y = i/100, i%100
    z = x + y
    if z**2==i:
        print("propriedade do 3025!")
    else:
        print("numero comum")