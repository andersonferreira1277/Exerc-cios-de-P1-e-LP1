#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
"""
Calcule os fatoriais de uma sequ�ncia de n�meros dada.

Formato de entrada
O programa receber� uma sequ�ncia de inteiros n, onde 0<=n<=12.
O programa encerra a sua execu��o quando o n�mero n dado for -1.

Para cada n, deve-se imprimir um inteiro k seguido de um final de linha, correspondendo ao fatorial.
"""
fatorial = 1
count = 1
num = []
while count != -1:
    count = int(input())
    if count != -1:
        num.append(count)
for i in num:
    fatorial = 1
    while i > 1:
        fatorial *= i
        i -= 1
    print(fatorial)