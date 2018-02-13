#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
O problema envolve achar a quantidade de divisores de um n�mero que s�o divis�veis por 3.

Formato de entrada
Um inteiro N.

Formato de sa�da
Um inteiro R seguido de um final de linha, sendo R o n�mero de divisores de N que s�o divisiveis por 3. Caso n�o tenha nenhum imprima "O numero nao possui divisores multiplos de 3!" sem as aspas e com um final de linha.
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