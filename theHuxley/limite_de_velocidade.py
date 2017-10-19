#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Devido ao grande n�mero de acidentes ocorridos recentemente na rua principal da cidade, um sistema de radares ser� instalado para multar os condutores que excederem os 50 km/h permitidos. Aqueles que excederem a velocidade, mas estiverem no m�ximo 10% acima da velocidade limite ser�o multados em R$ 230. J� os condutores que excederem a velocidade permitida em at� 20% ser�o multados em R$ 340. Caso a velocidade do motorista exceda o limite em mais de 20%, ele ter� que pagar uma multa de R$ 19,28 por cada km excedido.
Escreva uma fun��o chamada CalculaMulta que receba como entrada a velocidade de um condutor e retorne o valor da multa que ele ter� que pagar.

Formato de entrada
Um valor inteiro

Formato de sa�da
Um valor real
"""
def multa(v):
    if v <= 50:
        return 0.00
    elif v <= 50*0.10+50 and v > 50:
        return 230.00
    elif v > 50*0.10+50 and v <= 50*0.20+50:
        return 340.00
    elif v > 50*0.20+50:
        return (v-50)*19.28

num = float(input())
print ("%.2f" % (multa(num)))