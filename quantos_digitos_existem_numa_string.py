#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Voc� ir� receber uma string contendo letras e d�gitos. Sua miss�o � imprimir a quantidade de d�gitos que aparecem na string.

Formato de entrada
Uma linha com at� 200 caracteres contendo letras e n�meros

Formato de sa�da
Uma linha contendo um n�mero inteiro indicando a quantidade de d�gitos encontrados.
"""
entrada = raw_input()
nums = []
for i in entrada:
    if i.isdigit():
        nums.append(i)
print (len(nums))