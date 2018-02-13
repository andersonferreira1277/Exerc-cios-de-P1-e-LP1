#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Leia uma sequência de 101 números inteiros , verifique se o último número está presente nos 100 primeiros números e imprima as posições do array em que ele está presente.

Formato de entrada
Uma sequência de 101 números inteiros

Formato de saída
Uma sequência de inteiros separados por um final de linha, onde cada inteiro representa a posição do array em que foi encontrado o último número lido.
Se o último número não for encontrado nos 100 números anteriores não imprima nada
"""
count = 0
num = []
while count <= 100:
    num.append(int(input()))
    count += 1
for i in range(len(num)-1):
    if (num[i] == num[-1]):
        print(i)