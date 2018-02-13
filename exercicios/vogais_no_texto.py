#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Dado um texto como entrada, imprima a quantidade de cada uma das vogais presentes no texto.

Formato de entrada
Um texto/frase, com letras maiúsculas e minúsculas.

A quantidade de cada vogal encontrada no texto, uma em cada linha, no formato:
a 3
e 2
i 1
o 5
u 7
"""
palavra = raw_input()
palavra = palavra.lower()
count_A = 0
count_E = 0
count_I = 0
count_O = 0
count_U = 0
for i in palavra:
    if i == "a":
        count_A += 1
    elif i == "e":
        count_E += 1
    elif i == "i":
        count_I += 1
    elif i == "o":
        count_O += 1
    elif i == "u":
        count_U += 1
print("a %d" % count_A)
print ("e %d" % count_E)
print ("i %d" % count_I)
print ("o %d" % count_O)
print ("u %d" % count_U)