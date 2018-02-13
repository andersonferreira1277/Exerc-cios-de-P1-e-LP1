#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Faça um programa que leia três notas (valores reais) de um aluno, calcule sua média aritmética e imprima uma mensagem dizendo se o aluno foi aprovado, reprovado ou deverá fazer prova final. O critério de aprovação é o seguinte:
Aprovado (média >= 7);
Reprovado (média < 3);
Prova final ( 3 <= média < 7).

Formato de entrada
03 números reais separados por um final de linha.

Formato de saída
Uma mensagem que pode ser:
aprovado
reprovado
prova final
"""
a = float(input())
b = float(input())
c = float(input())
media = (a+b+c)/3
if 3 <= media < 7:
    print ("prova final")
elif media >= 7:
    print ("aprovado")
elif media < 3:
    print ("reprovado")