# -*- coding: latin1 -*-
# windows 10 64 bits
# python 2.7.12
# Feito por andersonferreira1277@gmail.com
"""
Descri��o
Leia valores inteiros. A seguir, calcule o produto entre estes valores e atribua esta opera��o � vari�vel PROD. A seguir mostre a vari�vel PROD com mensagem correspondente.

Formato de entrada
O arquivo de entrada cont�m n valores inteiros. Voc� n�o receber� um n�mero indicando quantos inteiros voc� receber�. Portanto, voc� dever� ler os n�meros at� n�o ter mais nenhum n�mero na entrada.
Embora essa quest�o seja simples, o desafio est� em descobrir usando a sua linguagem de programa��o, como voc� ir� ler os n�meros da entrada at� n�o ter mais entrada. Isso � diferente da maioria dos outros problemas do Huxley em que voc� sabe quando a entrada ir� terminar.

Formato de sa�da
Imprima a vari�vel PROD conforme exemplo abaixo, com um espa�o em branco antes e depois da igualdade. N�o esque�a o fim de linha ap�s o produto.
"""
prod = 1
try:
    while True:
        num = int(input())
        prod = num*prod
except:
    print ("Prod = %d\n" % prod)