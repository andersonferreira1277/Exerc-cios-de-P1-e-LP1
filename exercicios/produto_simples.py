# -*- coding: latin1 -*-
# windows 10 64 bits
# python 2.7.12
# Feito por andersonferreira1277@gmail.com
"""
Descrição
Leia valores inteiros. A seguir, calcule o produto entre estes valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.

Formato de entrada
O arquivo de entrada contém n valores inteiros. Você não receberá um número indicando quantos inteiros você receberá. Portanto, você deverá ler os números até não ter mais nenhum número na entrada.
Embora essa questão seja simples, o desafio está em descobrir usando a sua linguagem de programação, como você irá ler os números da entrada até não ter mais entrada. Isso é diferente da maioria dos outros problemas do Huxley em que você sabe quando a entrada irá terminar.

Formato de saída
Imprima a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça o fim de linha após o produto.
"""
prod = 1
try:
    while True:
        num = int(input())
        prod = num*prod
except:
    print ("Prod = %d\n" % prod)