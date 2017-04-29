#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Faça um programa que imprima todos os números (inteiros e positivos) entre x e y que satisfaçam as duas condições abaixo:
- não terminem em 0;
- se o dígito da direita for removido, o número restante é divisor do original.

Formato de entrada
Dois inteiros x e y, separados por um espaço. Onde: x>=10 e y<100.

Formato de saída
Os números inteiros (maiores ou iguais a x e menores ou iguais a y) que satisfazem as propriedades acima, separados por um final de linha.
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