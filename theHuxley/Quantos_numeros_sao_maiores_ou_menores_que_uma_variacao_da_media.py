#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Serão dados n números correspondendo as notas da turma de alunos de uma escola. Escreva um programa que leia essas notas e calcule quantas estão mais de 10% acima da média e quantas estão menos de 10% abaixo da média.

Formato de entrada
Na primeira linha você receberá um número inteiro n, onde n<=20000.
Em seguida você receberá n números reais, um em cada linha, correspondendo as notas de cada aluno da turma.

Formato de saída
Imprima na primeira linha da saída a média das notas formatada com duas casas decimais.
Na segunda linha imprima quantas notas ficaram mais de 10% acima da média.
Na terceira linha imprima quantas notas ficaram menos de 10% abaixo da média.
"""
count = int(input())
notas = []
resultado_abaixo = 0
resultado_acima = 0
while count > 0:
    notas.append(input())
    count -= 1
soma_notas = sum(notas)
quantidade_notas = float(len(notas))
media = soma_notas/quantidade_notas
media_acima = media*0.10+media
media_abaixo = media - media*0.10
for i in notas:
    if i > media_acima:
        resultado_acima += 1
    elif i < media_abaixo:
        resultado_abaixo += 1
print ("%.2f" % media)
print (resultado_acima)
print (resultado_abaixo)