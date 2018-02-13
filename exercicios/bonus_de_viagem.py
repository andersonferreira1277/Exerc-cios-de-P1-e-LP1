#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Lanne é uma funcionária dedicada e seu chefe prometeu-lhe um bônus especial de 75% de seu salário no fim do ano. Ela decidiu usar o dinheiro para fazer uma viagem, mas a escolha do destino dependerá do valor do bônus. Caso ela receba menos de R$ 2000, ela irá conhecer a Argentina. Já se o bônus for entre R$ 2000 e R$ 3000, ela irá para a Espanha. Se o bônus ganho for maior que R$ 3000, ela realizará o sonho de conhecer a Alemanha. Escreva um programa que receba como entrada o salário de Lanne e exiba o nome do país que ela irá conhecer.

Formato de entrada
Um número real com duas casas decimais

Formato de saída
Um String com todas as letras maiúsculas
"""
def viagem(b):
    if b < 2000:
        return "ARGENTINA"
    elif b >= 2000 and b <= 3000:
        return "ESPANHA"
    elif b > 3000:
        return "ALEMANHA"
salario = float(input())
print viagem(salario*0.75)