#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Todos os anos, os motoristas devem pagar ao Detran o IPVA (Imposto sobre a Propriedade de Ve�culos Automotores) e uma taxa de tr�nsito. Caso paguem o IPVA com anteced�ncia, recebem um desconto de 5% apenas no valor desse imposto. Escreva um programa que receba como entrada o valor do IPVA e o valor da taxa de tr�nsito, e exiba o total a ser pago por um motorista que deseja quitar sua d�vida cinco dias antes do prazo.

Formato de entrada
Dois valores reais, sendo o primeiro correspondente ao IPVA e o segundo correspondente � taxa de tr�nsito

Formato de sa�da
Um valor real com apenas duas casas decimais
"""
ipva = float(input())
taxa = float(input())
print ("%.2f" % ((ipva-ipva*0.05)+taxa))