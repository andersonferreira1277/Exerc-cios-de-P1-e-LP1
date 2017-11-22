#!/usr/bin/env python3
n1 = int(input("Digite a quantidade de acertos nas questões especificas\n"))
multiplicadorN1 = 50 / (50 - n1)
n1erro = int(input("Digite a quantidade de erros nas questões especificas\n"))
multiplicadorNegativoN1 = -(50 / (50 - n1erro))
print("Sua nota de acertos é:", n1 * multiplicadorN1)
print("Sua nota de acertos é:", n1 * multiplicadorNegativoN1)