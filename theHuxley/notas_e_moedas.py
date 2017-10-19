#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Formato de entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ? N ? 1000000.00).

Formato de saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

https://www.vivaolinux.com.br/topico/C-C++/Duvida-iniciante-3

http://pt.stackoverflow.com/questions/44715/como-arredondar-um-float-em-python
"""
count_100 = 0
count_50 = 0
count_20 = 0
count_10 = 0
count_5 = 0
count_2 = 0
count_1 = 0
count_050 = 0
count_025 = 0
count_010 = 0
count_005 = 0
count_001 = 0
#Inicialiazando com 0

valor = float(input())
if valor >= 100:
    count_100 = valor/100
    valor = round(valor%100,2)
if valor >= 50:
    count_50 = valor / 50
    valor = round(valor%50,2)
if valor >= 20:
    count_20 = valor/20
    valor = round(valor%20,2)
if valor >= 10:
    count_10 = valor/10
    valor = round(valor%10,2)
if valor >= 5:
    count_5 = valor/5
    valor = round(valor%5,2)
if valor >= 2:
    count_2 = valor/2
    valor = round(valor%2,2)
if valor >= 1:
    count_1 = valor/1
    valor = round(valor%1,2)
if valor >= 0.50:
    count_050 = valor/0.50
    valor = round(valor%0.50,2)
if valor >= 0.25:
    count_025 = valor/0.25
    valor = round(valor%0.25,2)
if valor >= 0.10:
    count_010 = valor/0.10
    valor = round(valor%0.10,2)
if valor >= 0.05:
    count_005 = valor/0.05
    valor = round(valor%0.05,2)
if True:
    count_001 = valor/0.01

print ("NOTAS:")
print ("%d nota(s) de R$ 100.00" % count_100)
print ("%d nota(s) de R$ 50.00" % count_50)
print ("%d nota(s) de R$ 20.00" % count_20)
print ("%d nota(s) de R$ 10.00" % count_10)
print ("%d nota(s) de R$ 5.00" % count_5)
print ("%d nota(s) de R$ 2.00" % count_2)
print ("MOEDAS:")
print ("%d moeda(s) de R$ 1.00" % count_1)
print ("%d moeda(s) de R$ 0.50" % count_050)
print ("%d moeda(s) de R$ 0.25" % count_025)
print ("%d moeda(s) de R$ 0.10" % count_010)
print ("%d moeda(s) de R$ 0.05" % count_005)
print ("%d moeda(s) de R$ 0.01" % round(count_001))