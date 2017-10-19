#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
O valor normal de um ingresso em um determinado cinema é R$ 20,00. Entretanto, se o cliente é estudante ou idoso, o cinema cobra apenas meia-entrada.
Faça um programa que leia um valor inteiro (0 ou 1) que indica se o cliente é estudante e outro valor inteiro (0 ou 1) que indica se o cliente é idoso. Com base nos valores lidos, o programa deve indicar, utilizando 0 ou 1, se este cliente paga entrada completa (falso - 0) ou meia-entrada (verdadeiro - 1).

Formato de entrada
Dois números inteiros (0 ou 1) separados por um fim de linha, indicando se o cliente é estudante e idoso, respectivamente.

Formato de saída
1 número inteiro (0 ou 1) indicando como deve ser o pagamento do cliente:
1 caso seja meia-entrada
0 caso seja entrada completa
"""
a = int(input())
b = int(input())
a = a+b
if a > 0:
    print("1")
else:
    print("0")