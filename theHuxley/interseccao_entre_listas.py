#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Faça um programa que recebe números de dois arrays inteiros com 20 posições cada e apresente a intersecção dos arrays ordenado de forma crescente. Lembrando que a intersecção são os elementos repetidos em ambos os arrays, mas sem repetição (cada número pode aparecer uma única vez no resultado).

Formato de entrada
Você receberá 40 números inteiros, um por linha, sendo 20 correspondendo ao primeiro array e 20 ao segundo.

Formato de saída
Você deve imprimir a intersecção entre os dois arrays, um número por linha, ordenado de forma crescente.
Caso a intersecção seja vazia, imprima a string "VAZIO"
"""
count = 1
nums = []
resultado = []
while count <=40:
    nums.append(int(input()))
    count += 1
for i in nums:
    if nums.count(i) > 1:
        if i in resultado:
            continue
        else:
            resultado.append(i)
    else:
        continue
resultado.sort()
if resultado == []:
    print ("VAZIO")
else:
    for x in resultado:
        print (x)
"""
OUtra forma:
for i in nums:
    if nums.count(i) > 1:
        resultado.append(i)
resultado = set(resultado)
if resultado == []:
    print ("VAZIO")
else:
    for x in resultado:
        print (x)
"""