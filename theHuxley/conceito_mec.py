#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Anualmente, o MEC avalia os cursos universit�rios de todo o pa�s e atribui conceitos com base em diversos crit�rios, sendo um deles a quantidade de livros dispon�veis. Considerando as regras definidas abaixo, escreva um programa que receba como entrada a quantidade de livros e a quantidade de alunos de um curso (nessa ordem) e exiba a letra mai�scula correspondente ao conceito concedido pelo MEC.
1 livro para at� 8 alunos --> Conceito A
1 livro para entre 9 e 12 alunos --> Conceito B
1 livro para entre 13 e 18 alunos --> Conceito C
1 livro para mais de 18 alunos --> Conceito D

Formato de entrada
Dois n�meros inteiros representando respectivamente a quantidade de livros e a quantidade de alunos.
Dica: lembre-se de n�o colocar mensagens no input

Formato de sa�da
Uma letra mai�scula correspondente ao conceito obtido.
Dica: lembre-se de n�o colocar mensagens no print
"""
a = float(input())
b = float(input())
r = b/a
if r <= 8:
    print("A")
elif (r >= 9) and (r <= 12):
    print("B")
elif (r >= 13) and (r <= 18):
    print("C")
elif (r > 18):
    print("D")