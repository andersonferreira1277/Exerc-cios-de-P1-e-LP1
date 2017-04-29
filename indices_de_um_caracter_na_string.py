#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição

Faça um progrma para ler uma string e um caracter qualquer e imprima as posições (índices) de onde ocorre o caracter na string. Por exemplo, seja a string "abracadabra!!!" e o caracter 'a', então a sua saída deve ser:

0
3
5
7
10
-1
O valor -1 indica o final, ou seja, não existem mais ocorrências. Caso não exista nenhuma ocorrência, deve ser impresso o valor -1.
Considere também que o 0 representa o índice do primeiro caracter em uma string.

Formato de entrada
Você receberá duas linhas. A primeira linha contém a string e a segunda linha contém um caracter. O tamanho máximo da string é 50.

Formato de saída
Imprima os índices, sendo um por linha.
"""
a = raw_input()
b = raw_input()
indice = 0
count = 0
for i in a:
    if i == b:
        print indice
    indice += 1
print -1