#-*- coding: latin1 -*-
# windows 10 64 bits
#python 2.7.12
"""
Toda vez que Ambr�sio vai calcular as ra�zes de uma equa��o do segundo grau,
esquece de algum detalhe e calcula errado.
Para evitar esquecimentos, resolveu fazer um programa que calcula
as ra�zes da equa��o de segundo grau.

Consiste dos n�meros reais a, b e c, que correspondem aos coeficientes da equa��o de segundo grau (ax�+bx+c=0).

============================Calculo=======================
calculo de delta - delta = b�-4ac
raiz_de_delta = delta ** 0.5
x1 = (-b + raiz_de_delta) / (2*a)
x2 = (-b - raiz_de_delta) / (2*a)

Formato de entrada

Consiste dos n�meros reais a, b e c, que correspondem aos coeficientes da equa��o de segundo grau (ax�+bx+c=0).

Formato de sa�da

Caso existam as ra�zes da equa��o, consiste de dois n�meros reais formatados com duas casas decimais, representando as mesmas.
Caso as ra�zes n�o existam, o sistema deve mostrar a mensagem (n�o existem ra�zes reais): NRR
Caso n�o seja uma equa��o de segundo grau, o sistema deve mostrar a mensagem (n�o � uma equa��o do segundo grau): NEESG
"""

a = float(input())
b = float(input())
c = float(input())
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("NRR")
elif delta >= 0 and a!=0:
    raiz_de_delta = delta ** 0.5
    x1 = (-b + raiz_de_delta) / (2*a)
    x2 = (-b - raiz_de_delta) / (2*a)
    print("%.2f" % x1)
    print("%.2f" % x2)
elif delta==0 and a!=0:
    raiz_de_delta = delta ** 0.5
    x1 = (-b + raiz_de_delta) / (2 * a)
    print("%.2f" % x1)
else:
    print("NEESG")
