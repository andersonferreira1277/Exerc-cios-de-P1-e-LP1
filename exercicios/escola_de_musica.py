#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
A Escola de M�sica Melodia � bastante conceituada na cidade e forma grandes profissionais. Para isso, exige que seus alunos tenham no m�ximo 10 faltas por semestre, e que obtenham m�dia m�nima 7 para serem aprovados. Aqueles que n�o excedem o limite de faltas e conseguem m�dia igual ou superior a 9,5 s�o aprovados com louvor.
Escreva uma fun��o chamada ClassificaAluno que receba como entrada a media e a quantidade de faltas de um aluno e retorne sua situa��o ao final do semestre.

Formato de entrada
Um n�mero real e um n�mero inteiro, nessa ordem

Formato de sa�da
Um String em letras mai�sculas (APROVADO COM LOUVOR ou APROVADO ou REPROVADO ou REPROVADO POR FALTAS)
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
