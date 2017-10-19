#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
O problema envolve achar a quantidade de divisores de um número que são divisíveis por 3.

Formato de entrada
Um inteiro N.

Formato de saída
Um inteiro R seguido de um final de linha, sendo R o número de divisores de N que são divisiveis por 3. Caso não tenha nenhum imprima "O numero nao possui divisores multiplos de 3!" sem as aspas e com um final de linha.
"""
n = int(input())
count = []
for i in range(1,n+1):
    if (n % i == 0) and (i % 3 == 0):
        count.append(i)
    else:
        continue
if not count == []:
    print (len(count))
else:
    print ("O numero nao possui divisores multiplos de 3!")