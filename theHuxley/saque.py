#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Crie um programa que gerencie a sa�da de notas em um caixa eletr�nico.
Recebendo a quantia, seu programa deve dizer quantas de cada nota devem ser retiradas. Utilize o crit�rio da "distribui��o �tima", ou seja, o menor n�mero poss�vel de c�dulas. O caixa tem c�dulas de R$50, R$20, R$10, R$5 e R$1.

Entrada
Um inteiro n representando a quantia a ser sacada

Sa�da
Notas de 50: X
Notas de 20: Y
Notas de 10: Z
Notas de 5: W
Notas de 1: K
onde X, Y, Z, W e K devem ser substitu�dos por n�meros inteiros que correspondem a quantidade de notas
"""
#entrada
nota = int(input())
# iniciar todas as notas com 0
x, y, z, w, k = 0, 0, 0, 0, 0
if nota>= 50:
    x = nota//50
    nota = nota%50
if nota>= 20:
    y = nota//20
    nota = nota%20
if nota>= 10:
    z = nota//10
    nota = nota%10
if nota>= 5:
    w = nota//5
    nota = nota%5
if nota>= 1:
    k = nota//1
print("Notas de 50: %d" % x)
print("Notas de 20: %d" % y)
print("Notas de 10: %d" % z)
print("Notas de 5: %d" % w)
print("Notas de 1: %d" % k)