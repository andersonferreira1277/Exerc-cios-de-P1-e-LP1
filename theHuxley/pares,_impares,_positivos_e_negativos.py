#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Leia um valor inteiro N. Depois, imprima uma mensagem dizendo que se este valor for �mpar, par, positivo, negativo ou nulo.
A mensagem deve estar em letras mai�sculas.

Formato de entrada
Um n�mero N.
Considere que o maior inteiro que voc� poder� receber � 10^12 (10 elevado a 12)

Formato de sa�da
Uma frase, informando se o n�mero � POSITIVO PAR, POSITIVO IMPAR, NEGATIVO PAR, NEGATIVO IMPAR ou NULO.
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