#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
No frigorífico do senhor Ambrósio, existem n bois. Cada boi traz preso
 em seu pescoço um cartão contendo seu número de identificação e seu 
 peso. Faça um programa que escreva a identificação e o peso do boi mais
  gordo e do mais magro. Considere que os bois não têm pesos iguais.
  
Um inteiro n indicando a quantidade de bois do frigorifico, depois n 
identificadores e pesos de cada boi. Os identificadores são números 
inteiros. Os pesos de cada boi são números reais.

Duas linhas escritas:


Gordo: id: i1 peso: p1Kg
Magro: id: i2 peso: p2Kg

O peso deve ser formatado em duas casas decimais.
'''
tamanho = int(input())
count = 1
dict = {}
while count <= tamanho:
	 boi = raw_input().split()
	 dict[boi[0]] = float(boi[1])
	 count +=1
print ('Gordo: id: %s peso: %.2fKg' % (max(dict),max(dict.values())))
print ('Magro: id: %s peso: %.2fKg' % (min(dict),min(dict.values())))
