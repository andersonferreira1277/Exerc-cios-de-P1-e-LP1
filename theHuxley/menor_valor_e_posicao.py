#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Escrever um programa que lê um número N. Este N é o tamanho de um array.
Em seguida, leia cada um dos N números do array, encontre o menor elemento desse array, a sua posição dentro do array e imprima essas informações.
Considere que o array começa na posição 0

A primeira linha da entrada contém um inteiro N (1 <N <1000), indicando o número de elementos que devem ser lidos no array de números inteiros. A segunda linha contém cada um dos valores de N, separadas por um espaço.
Obs: não haverão números repetidos.

A primeira linha exibe a mensagem "Menor valor:" seguido por um espaço e o menor número lido na entrada. A segunda linha exibe a mensagem "POSIÇÃO:" seguido por um espaço e a posição do array em que o menor número é encontrado, lembrando que o array começa na posição zero.
'''
tamanho = int(input())
lista = map(int, raw_input().split())
print ('Menor valor: %d' % (min(lista)))
print ('Posicao: %d' % (lista.index(min(lista))))
