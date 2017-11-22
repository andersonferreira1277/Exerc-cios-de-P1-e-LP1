#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Todos os anos, os motoristas devem pagar ao Detran o IPVA (Imposto sobre a Propriedade de Veículos Automotores) e uma taxa de trânsito. Caso paguem o IPVA com antecedência, recebem um desconto de 5% apenas no valor desse imposto. Escreva um programa que receba como entrada o valor do IPVA e o valor da taxa de trânsito, e exiba o total a ser pago por um motorista que deseja quitar sua dívida cinco dias antes do prazo.

Formato de entrada
Dois valores reais, sendo o primeiro correspondente ao IPVA e o segundo correspondente à taxa de trânsito

Formato de saída
Um valor real com apenas duas casas decimais
"""
ipva = float(input())
taxa = float(input())
print ("%.2f" % ((ipva-ipva*0.05)+taxa))