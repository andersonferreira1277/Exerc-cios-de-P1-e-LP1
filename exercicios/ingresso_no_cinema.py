#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
O valor normal de um ingresso em um determinado cinema � R$ 20,00. Entretanto, se o cliente � estudante ou idoso, o cinema cobra apenas meia-entrada.
Fa�a um programa que leia um valor inteiro (0 ou 1) que indica se o cliente � estudante e outro valor inteiro (0 ou 1) que indica se o cliente � idoso. Com base nos valores lidos, o programa deve indicar, utilizando 0 ou 1, se este cliente paga entrada completa (falso - 0) ou meia-entrada (verdadeiro - 1).

Formato de entrada
Dois n�meros inteiros (0 ou 1) separados por um fim de linha, indicando se o cliente � estudante e idoso, respectivamente.

Formato de sa�da
1 n�mero inteiro (0 ou 1) indicando como deve ser o pagamento do cliente:
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