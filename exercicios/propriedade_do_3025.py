#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Repare a seguinte caracter�stica do n�mero 3025:
30 + 25 = 55 e 55^2 = 3025
Fa�a um programa que leia uma s�rie de valores (n�meros inteiros de 4 d�gitos, um de cada vez) e diga se possuem a mesma caracter�stica. O programa termina quando for lido um valor menor que 1000 ou maior que 9999.

Formato de entrada
Uma sequ�ncia de n�meros inteiros, separados por um final de linha

Formato de sa�da
Para cada n�mero lido, seu programa deve imprimir:
"propriedade do 3025!", caso o n�mero lido atenda � propriedade descrita acima, ou "numero comum" caso contr�rio.
Imprima um final de linha ap�s cada sa�da.
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