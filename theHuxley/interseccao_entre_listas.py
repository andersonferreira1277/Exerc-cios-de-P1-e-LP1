#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Fa�a um programa que recebe n�meros de dois arrays inteiros com 20 posi��es cada e apresente a intersec��o dos arrays ordenado de forma crescente. Lembrando que a intersec��o s�o os elementos repetidos em ambos os arrays, mas sem repeti��o (cada n�mero pode aparecer uma �nica vez no resultado).

Formato de entrada
Voc� receber� 40 n�meros inteiros, um por linha, sendo 20 correspondendo ao primeiro array e 20 ao segundo.

Formato de sa�da
Voc� deve imprimir a intersec��o entre os dois arrays, um n�mero por linha, ordenado de forma crescente.
Caso a intersec��o seja vazia, imprima a string "VAZIO"
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