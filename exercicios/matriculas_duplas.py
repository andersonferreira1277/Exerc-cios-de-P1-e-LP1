#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
A coordenação do curso de Ciência da Computação da UFAL deseja saber quantos alunos estão cursando ao mesmo tempo as cadeiras de Programação II e Programação III. Faça um programa que leia os códigos de matrícula dos alunos de ambos os cursos e imprima os códigos de matrículas dos alunos que estão cursando ambas as disciplinas.
Sabe-se que a disciplina de Programação II conta com 45 alunos e a disciplina de Programação III conta com 30 alunos.

Formato de entrada
Uma sequência de 45 inteiros representando as matrículas dos alunos cursando a disciplina de Programação II, seguida de uma sequência de 30 inteiros representando as matrículas dos alunos que cursam a disciplina de Programação III.

Formato de saída
Uma lista de inteiros correspondendo aos alunos que estão matriculados em ambas as disciplinas.
Cada inteiro deve ser separado por um espaço. Após o último inteiro, deve existir um espaço seguido de um final de linha.
As matrículas devem ser impressas de acordo com a ordem dada na entrada da disciplina de Programação II.
"""
a = raw_input()
b = raw_input()
b = b.split()
b = map(int, b)
a = a.split()
a = map(int, a)
a = a+b
resposta = []
apre = ""
for i in a:
    if a.count(i) > 1:
        if not i in resposta:
            resposta.append(i)
        else:
            continue
for x in range(len(resposta)):
    if x < len(resposta):
        apre = apre + str(resposta[x]) + " "
    else:
        apre = apre + str(resposta[x])
print (apre)