#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
A Escola de Música Melodia é bastante conceituada na cidade e forma grandes profissionais. Para isso, exige que seus alunos tenham no máximo 10 faltas por semestre, e que obtenham média mínima 7 para serem aprovados. Aqueles que não excedem o limite de faltas e conseguem média igual ou superior a 9,5 são aprovados com louvor.
Escreva uma função chamada ClassificaAluno que receba como entrada a media e a quantidade de faltas de um aluno e retorne sua situação ao final do semestre.

Formato de entrada
Um número real e um número inteiro, nessa ordem

Formato de saída
Um String em letras maiúsculas (APROVADO COM LOUVOR ou APROVADO ou REPROVADO ou REPROVADO POR FALTAS)
"""
def ClassificaAluno(n,f):
    if n >= 9.5 and f <= 10:
        return "APROVADO COM LOUVOR"
    elif f <= 10 and n >= 7:
        return "APROVADO"
    elif n < 7:
        return "REPROVADO"
    elif True:
        return "REPROVADO POR FALTAS"
nota = float(input())
faltas = int(input())
print ClassificaAluno(nota,faltas)
