#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Seu programa deve receber um vetor de N valores inteiros e imprimir na ordem inversa.

Formato de entrada
Na primeira linha de entrada o programa recebe um valor inteiro N de entrada. A segunda linha cont�m N inteiros separados por espa�o contendo os valores do array.

Formato de sa�da
Uma linha contendo os n�meros do vetor em ordem invertida separados por espa�os em branco, seguida de um final de linha.
Depois do �ltimo n�mero, n�o deve existir um espa�o em branco.
"""
nda = int(input())
a = raw_input()
a = a.split()
resposta = ""
a = a[::-1]
for i in range(len(a)):
    if i < range(len(a)-1):
        resposta = resposta + str(a[i]) + " "
    else:
        resposta = resposta + str(a[i])
print(resposta)