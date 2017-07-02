#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Formato de entrada
Quatro números inteiros A, B, C e D.

Formato de saída
Mostre a respectiva mensagem após a validação dos valores.
"""
a,b,c,d = map(int, raw_input().split())
if b > c and d > a and c+d > a+b and c > -1 and d > -1 and a % 2 == 0:
    print ("Valores aceitos")
else:
    print ("Valores nao aceitos")