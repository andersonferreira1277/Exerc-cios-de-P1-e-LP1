# *-* coding: latin1 -*-
# Windows 10 64 bits
# python 2.7.12
"""
Fa�a um programa que leia dois n�meros inteiros, representando os valores inicio e fim de um
intervalo e imprima os m�ltiplos de 5 entre eles.

formato de entrada: Dois n�meros inteiros, n e m, separados por um espa�o.

formato de sa�da: Todos os m�ltiplos de 5, maiores ou iguais a n e menores ou iguais a m, separados pelo caractere '|'.
Note que depois do �ltimo m�ltiplo, n�o existe o caractere '|'.

"""
entrada = raw_input()
a, b = entrada.split()
resposta = []
a = int(a)
b = int(b)
resposta_f = ""
for x in range(a, b + 1):
    if x % 5 == 0:
        resposta.append(x)
teste = len(resposta)
for i in range(len(resposta)):
    if i < len(resposta)-1:
        resposta_f = resposta_f + str(resposta[i]) + "|"
    else:
        resposta_f = resposta_f + str(resposta[i])
print(resposta_f)