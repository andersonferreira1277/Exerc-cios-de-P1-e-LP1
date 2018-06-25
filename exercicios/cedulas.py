#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Formato de entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Formato de saída
Imprima a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
"""
count_100 = 0
count_50 = 0
count_20 = 0
count_10 = 0
count_5 = 0
count_2 = 0
count_1 = 0
def Notas(v):
    global count_100
    global count_50
    global count_20
    global count_10
    global count_5
    global count_2
    global count_1
    if v >= 100:
        count_100 = v/100
        v = v%100.0
    if v >= 50:
        count_50 = v/50
        v = v%50.0
    if v >= 20:
        count_20 = v/20
        v = v%20.0
    if v >= 10:
        count_10 = v/10
        v = v%10.0
    if v >= 5:
        count_5 = v/5
        v = v % 5.0
    if v >= 2:
        count_2 = v/2
        v = v % 2.0
    if True:
        count_1 = v/1
valor = int(input())
print(valor)
Notas(valor)
print ("%d nota(s) de R$ 100,00" % count_100)
print ("%d nota(s) de R$ 50,00" % count_50)
print ("%d nota(s) de R$ 20,00" % count_20)
print ("%d nota(s) de R$ 10,00" % count_10)
print ("%d nota(s) de R$ 5,00" % count_5)
print ("%d nota(s) de R$ 2,00" % count_2)
print ("%d nota(s) de R$ 1,00" % count_1)