#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
     A biblioteca de Rio Tinto empresta gratuitamente seus livros a alunos, professores e funcionários de todo o campus. Entretanto, sempre que um usuário atrasa a entrega de um livro, ele tem que pagar uma multa de R$ 0,75 por cada dia de atraso.
Escreva um programa que receba como entrada a quantidade de dias de atraso do empréstimo de um livro, e exiba o valor da multa a ser paga pelo usuário.

Formato de entrada
Valor inteiro representando a quantidade de dias de atraso.

Formato de saída
Você deve imprimir um valor real formatado com duas casas decimais, representando o valor da multa a ser paga.
"""
a = int(input())
r = a*0.75
print("%.2f" % r)