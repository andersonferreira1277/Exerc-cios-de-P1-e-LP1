#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Poliana resolveu economizar dinheiro para comprar um carro.
Ela traçou como meta depositar um valor X em seu cofrinho no primeiro dia da semana, e ir guardando a cada manhã o valor do dia anterior acrescido de pelo menos R$ 0,50. Mas será que ela vai conseguir fazer isso todos os dias?
Para saber se o plano de Poliana vai dar certo, escreva um programa que receba como entrada o valor inicial depositado, e em seguida os valores depositados a cada dia. Ao final, exiba o total poupado e quantas vezes Poliana conseguiu cumprir sua meta.
Dica: é preciso sempre comparar o valor do dia com o do dia anterior

Formato de entrada
Valores reais, um para cada dia da semana

Formato de saída
Um valor real com duas casas decimais precedido pelo símbolo R$ (Ex: R$ 7.80)
Um valor inteiro indicando em quantos dias Poliana cumpriu sua meta
"""
count = 1
count2 = 0
valor = 0
dia_anterior = 0
while count <= 7:
    depo = float(input())
    valor = depo + valor
    if depo - dia_anterior>= 0.50 and count != 1:
        count2 += 1
    count += 1
    dia_anterior = depo
print ("R$ %.2f" % valor)
print count2