#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Leia um valor inteiro N. Depois, imprima uma mensagem dizendo que se este valor for ímpar, par, positivo, negativo ou nulo.
A mensagem deve estar em letras maiúsculas.

Formato de entrada
Um número N.
Considere que o maior inteiro que você poderá receber é 10^12 (10 elevado a 12)

Formato de saída
Uma frase, informando se o número é POSITIVO PAR, POSITIVO IMPAR, NEGATIVO PAR, NEGATIVO IMPAR ou NULO.
Seguido de uma quebra de linha.
"""
def par_impar(num):
    if (num%2 == 0):
        return "PAR"
    else:
        return "IMPAR"
def positivo_negativo(num):
    if num > 0:
        return "POSITIVO"
    else:
        return "NEGATIVO"

num = input()
if (num == 0):
    print ("NULO")
else:
    print (positivo_negativo(num) + " " + par_impar(num))