#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Fa�a um programa que imprima todos os n�meros (inteiros e positivos) entre x e y que satisfa�am as duas condi��es abaixo:
- n�o terminem em 0;
- se o d�gito da direita for removido, o n�mero restante � divisor do original.

Formato de entrada
Dois inteiros x e y, separados por um espa�o. Onde: x>=10 e y<100.

Formato de sa�da
Os n�meros inteiros (maiores ou iguais a x e menores ou iguais a y) que satisfazem as propriedades acima, separados por um final de linha.
"""
# recebendo a entrada=============================================================
entrada = raw_input()
entrada = entrada.split()
num = []
for i in entrada:
    num.append(int(i))
# =================================================================================
for i in range(num[0],num[1]+1):
    if (i >= 0) and (i % 10 != 0) and (i % (i/10) ==0):
        print(i)