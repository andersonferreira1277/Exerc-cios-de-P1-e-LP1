#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Nos parques de divers�o, alguns brinquedos tem idade e altura m�nimas para poder andar neles.
O parque Ambrol�ndia possui 3 brinquedos que possuem essa limita��o:
Barca Viking: 1,5m de altura e 12 anos.
Elevator of Death: 1,4m de altura e 14 anos.
Final Killer: 1,7m de altura ou 16 anos.
Dada a altura e a idade de uma pessoa, fa�a um programa que identifique quantos brinquedos ele pode andar.

Formato de entrada
Dois inteiros, F e I, representando a altura (em cm) e a idade, respectivamente.

Formato de sa�da
O n�mero de brinquedos que ele pode andar no parque, seguido de uma quebra de linha.
"""
#===============================entrada=============================================
a = raw_input()
a = a.split()
b = []
for i in a:
    b.append(int(i))
#===================================================================================
brinquedos = 0
if b[0] >= 150 and b[1] >= 12:
    brinquedos += 1
if b[0] >= 140 and b[1] >= 14:
    brinquedos += 1
if b[0] >= 170 or b[1] >= 16:
    brinquedos += 1
print(brinquedos)