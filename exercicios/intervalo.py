#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
O arquivo de entrada contém um valor real qualquer. O programa deve apresentar uma mensagem dizendo em qual dos seguintes intervalos: [0,25] (25,50], (50,75], (75,100]. Se o valor for menor do que 0 ou maior do que 100 deve ser apresentada uma mensagem ?Fora de intervalo?.
Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000
Ou seja, os símbolos [ e ] são usados para representar o intervalo fechado e os símbolos ( e ) para intervalos abertos.

Formato de entrada
O arquivo de entrada contém um número com ponto flutuante qualquer.

Formato de saída
A saída deve ser uma mensagem conforme exemplo de saída.
"""
#(50,75], (75,100]
a = float(input())
if (a >= 0) and (a <= 25.0000):
    print("Intervalo [0,25]")
elif (a > 25.0000) and (a <= 50.0000000):
    print("Intervalo (25,50]")
elif (a > 50.0000000) and (a <= 75.00):
    print("Intervalo (50,75]")
elif (a > 75.00) and (a <= 100.00):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")