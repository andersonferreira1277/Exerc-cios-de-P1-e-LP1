#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Lanne � uma funcion�ria dedicada e seu chefe prometeu-lhe um b�nus especial de 75% de seu sal�rio no fim do ano. Ela decidiu usar o dinheiro para fazer uma viagem, mas a escolha do destino depender� do valor do b�nus. Caso ela receba menos de R$ 2000, ela ir� conhecer a Argentina. J� se o b�nus for entre R$ 2000 e R$ 3000, ela ir� para a Espanha. Se o b�nus ganho for maior que R$ 3000, ela realizar� o sonho de conhecer a Alemanha. Escreva um programa que receba como entrada o sal�rio de Lanne e exiba o nome do pa�s que ela ir� conhecer.

Formato de entrada
Um n�mero real com duas casas decimais

Formato de sa�da
Um String com todas as letras mai�sculas
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