#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Ambr�sio � amigo da vizinhan�a e resolveu dar descontos para agradar seus clientes. A mercearia de Ambr�sio cont�m apenas 04 itens, cujos pre�os s�o dados pela tabela abaixo:
A regra de desconto � bem simples: se a quantidade de produtos comprados for igual ou maior que quinze, ent�o o desconto � concedido. O desconto tamb�m � concedido caso o valor total da compra seja maior ou igual a 40 reais.
O valor do desconto � de 15%.
Sua miss�o � fazer um programa que leia o c�digo do produto, a quantidade comprada e imprima o valor que o cliente deve pagar, j� considerando o desconto quando aplic�vel.
Considere que o cliente s� pode comprar um �nico tipo produto cada vez que usar o seu software.
1 = 5,30
2 = 6,00
3 = 3,20
4 = 2,50

Formato de entrada
Um n�mero inteiro correspondendo ao c�digo do produto, seguido de um inteiro indicando a quantidade comprada.
Os inteiros s�o separados por um final de linha.

Formato de sa�da
A sa�da deve conter o seguinte formato:
R$ x
Onde x corresponde a um n�mero real formatado com duas casas decimais, indicando o valor a ser pago pelo cliente.
A sua sa�da deve ser seguida de um final de linha.
Obs.: perceba que existe um espa�o entre o $ e o n�mero x.
"""
#====Definir valor a =======================================================
def valor(a):
    if a == 1:
        a = 5.30
        return a
    elif a == 2:
        a = 6.00
        return a
    elif a == 3:
        a = 3.20
        return a
    elif a == 4:
        a = 2.50
        return a
    else:
        print("C�digo invalido")
#======================================entrada=============================
a = int(input())
b = int(input())
a = valor(a)
#=============================================================================
if (b == 15) or (a*b >= 40.00):
    total = (a*b)-(((a * b)*15)/100)
else:
    total = a*b
print("R$ %.2f" % total)