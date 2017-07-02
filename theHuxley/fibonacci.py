#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
A sequ�ncia de Fibonacci � definida pela seguinte sequ�ncia: 0 1 1 2 3 5 8 13 21... Em que cada termo da sequ�ncia � obtido somando os dois termos anteriores.
Escreva um programa que imprima os n primeiros termos da sequ�ncia dos n�meros Fibonacci.

Formato de entrada
Um n�mero inteiro n indicando a quantidade de termos da sequ�ncia de fibonacci a serem impressos. Onde: 0<=n <=47.
A entrada termina quando n=0

Formato de sa�da
A sequ�ncia de termos da s�rie fibonacci. Cada termo � separado por um espa�o.
Depois do �ltimo termo n�o deve existir espa�o.
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