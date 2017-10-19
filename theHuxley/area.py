#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Escreva um programa que leia três valores com ponto flutuante: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e c por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Formato de entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Formato de saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
"""
import math
def triangulo(num1,num2):
    resultado = (num1*num2)/2
    print ("TRIANGULO: %.3f" % resultado)

def circulo(num1):
    resultado = 3.14159*num1**2
    print ("CIRCULO: %.3f" % resultado)

def trapezio(num1,num2,num3):
    resultado = ((num1+num2)*num3)/2
    print ("TRAPEZIO: %.3f" % resultado)

def quadrado(num1):
    resultado = num1**2
    print ("QUADRADO: %.3f" % resultado)

def retangulo(num1,num2):
    resultado = num1*num2
    print ("RETANGULO: %.3f" % resultado)

#======================main==========================
entrada = raw_input()
entrada = entrada.split()
entrada = map(float, entrada)
triangulo(entrada[0],entrada[2])
circulo(entrada[2])
trapezio(entrada[0],entrada[1],entrada[2])
quadrado(entrada[1])
retangulo(entrada[0],entrada[1])