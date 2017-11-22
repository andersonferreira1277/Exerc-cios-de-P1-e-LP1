#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Berenice é professora de 7 turmas do Ensino Médio. Em cada turma, ela realiza 4 provas por ano. Ela resolveu fazer uns cálculos de quantos grampos ela vai gastar para grampear todas as provas do ano que vem.
Escreva um programa que receba como entrada a quantidade de alunos de cada turma de Berenice, e exiba o total de grampos que serão usados e a quantidade de caixas que ela precisará adquirir (cada caixa contém 30 grampos).
Obs: Considere que todos os alunos farão todas as provas, e que todas as provas precisam ser grampeadas, sem exceções

Formato de entrada
Vários valores inteiros

Formato de saída
Dois valores inteiros
"""
import math
count = 1
num = []
while count <= 7:
    num.append(int(input()))
    count += 1
total = sum(num)*4
print total
print ("%d" % (math.ceil(total/30.0)))