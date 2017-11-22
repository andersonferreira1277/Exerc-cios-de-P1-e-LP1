#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
A sequência de Fibonacci é definida pela seguinte sequência: 0 1 1 2 3 5 8 13 21... Em que cada termo da sequência é obtido somando os dois termos anteriores.
Escreva um programa que imprima os n primeiros termos da sequência dos números Fibonacci.

Formato de entrada
Um número inteiro n indicando a quantidade de termos da sequência de fibonacci a serem impressos. Onde: 0<=n <=47.
A entrada termina quando n=0

Formato de saída
A sequência de termos da série fibonacci. Cada termo é separado por um espaço.
Depois do último termo não deve existir espaço.
"""
def fibonacci(l):
    count = 1
    lista = []
    temp = ""
    a, b = 0, 1
    while count <= l:
        lista.append(a)
        a, b = b, a + b
        count += 1
    for i in lista:
        if lista.index(i) < len(lista) - 1:
            temp = temp + str(i) + " "
        else:
            temp = temp + str(i)
    return temp
limite = []
while True:
    temp_limite = long(input())
    if temp_limite == 0:
        break
    elif 0<=temp_limite<=47:
        limite.append(temp_limite)
for x in limite:
    print fibonacci(x)