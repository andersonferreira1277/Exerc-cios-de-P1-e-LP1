#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Fa�a um programa que leia tr�s notas (valores reais) de um aluno, calcule sua m�dia aritm�tica e imprima uma mensagem dizendo se o aluno foi aprovado, reprovado ou dever� fazer prova final. O crit�rio de aprova��o � o seguinte:
Aprovado (m�dia >= 7);
Reprovado (m�dia < 3);
Prova final ( 3 <= m�dia < 7).

Formato de entrada
03 n�meros reais separados por um final de linha.

Formato de sa�da
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