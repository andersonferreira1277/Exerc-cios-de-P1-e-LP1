#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Dado um conjunto de n valores inteiros, ordene-os em ordem crescente.

Formato de entrada
Um inteiro n indicando quantos n�meros ser�o fornecidos, seguidos de n inteiros separados por um final de linha

Formato de sa�da
A sequ�ncia de n n�meros ordenada em ordem crescente, obedecendo ao seguinte formato:
[numero][numero][numero][numero]
Onde depois do �ltimo n�mero existe um final de linha.
"""
n = int(input())
count = 1
nums = []
while count <= n:
    entrada = int(input())
    nums.append(entrada)
    count += 1
nums.sort()
resultado = ""
for i in nums:
    resultado = resultado + "[" + str(i) + "]"
print resultado
