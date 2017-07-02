#-*- coding: latin1 -*-
# windows 10 64 bits
#python 2.7.12
"""
Toda vez que Ambrósio vai calcular as raízes de uma equação do segundo grau,
esquece de algum detalhe e calcula errado.
Para evitar esquecimentos, resolveu fazer um programa que calcula
as raízes da equação de segundo grau.

Consiste dos números reais a, b e c, que correspondem aos coeficientes da equação de segundo grau (ax²+bx+c=0).

============================Calculo=======================
calculo de delta - delta = b²-4ac
raiz_de_delta = delta ** 0.5
x1 = (-b + raiz_de_delta) / (2*a)
x2 = (-b - raiz_de_delta) / (2*a)

Formato de entrada

Consiste dos números reais a, b e c, que correspondem aos coeficientes da equação de segundo grau (ax²+bx+c=0).

Formato de saída

Caso existam as raízes da equação, consiste de dois números reais formatados com duas casas decimais, representando as mesmas.
Caso as raízes não existam, o sistema deve mostrar a mensagem (não existem raízes reais): NRR
Caso não seja uma equação de segundo grau, o sistema deve mostrar a mensagem (não é uma equação do segundo grau): NEESG
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
