#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Leia uma sequ�ncia de 101 n�meros inteiros , verifique se o �ltimo n�mero est� presente nos 100 primeiros n�meros e imprima as posi��es do array em que ele est� presente.

Formato de entrada
Uma sequ�ncia de 101 n�meros inteiros

Formato de sa�da
Uma sequ�ncia de inteiros separados por um final de linha, onde cada inteiro representa a posi��o do array em que foi encontrado o �ltimo n�mero lido.
Se o �ltimo n�mero n�o for encontrado nos 100 n�meros anteriores n�o imprima nada
"""
count = 0
num = []
while count <= 100:
    num.append(int(input()))
    count += 1
for i in range(len(num)-1):
    if (num[i] == num[-1]):
        print(i)