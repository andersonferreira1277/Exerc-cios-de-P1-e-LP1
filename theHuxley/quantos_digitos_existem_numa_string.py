#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Você irá receber uma string contendo letras e dígitos. Sua missão é imprimir a quantidade de dígitos que aparecem na string.

Formato de entrada
Uma linha com até 200 caracteres contendo letras e números

Formato de saída
Uma linha contendo um número inteiro indicando a quantidade de dígitos encontrados.
"""
entrada = raw_input()
nums = []
for i in entrada:
    if i.isdigit():
        nums.append(i)
print (len(nums))