#!/usr/bin/python3
numero = int(input('Digite um número para saber sua tabuada\n'))
for x in range(1,11):
    print('{} X {} = {:1.1f}'.format(numero, x,numero*x))