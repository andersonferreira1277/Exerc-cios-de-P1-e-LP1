#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Leia duas strings e verifique o número de ocorrências da segunda string na primeira. Exemplo: Se a primeira string digitada for "abracadabra" e a segunda "bra", então o número de ocorrências é 2.

Formato de entrada
Você receberá duas linhas. Cada linha com uma string.

Formato de saída
Você deve imprimir um número inteiro indicando o número de ocorrências encontradas.
Imprima também o final de linha.
"""
a = raw_input()
b = raw_input()
print a.count(b)
