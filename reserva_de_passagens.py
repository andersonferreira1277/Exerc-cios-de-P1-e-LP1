#-*- coding: latin1 -*-
#kubuntu 16.04 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
O cenário é uma terra muito distante, onde ainda ocorre o caos aéreo. Você, é o desenvolvedor de software responsável pelos sistemas da Ambrosino Airlines. Sua missão é desenvolver um sistema de reserva de passagens. A Ambrosino Airlines possui 37 voos fixos.

Uma sequência de 37 pares de inteiros, indicando o número do voo e a quantidade de lugares disponíveis no respectivo voo. Depois você lerá uma sequência de pedidos de reserva. Cada pedido de reserva é representado por um par de inteiros indicando, respectivamente, o número do documento de identidade do cliente e o número do voo que o cliente deseja viajar. A entrada se encerra quando o número do documento de identidade do cliente for igual a 9999. Existe a possibilidade de que o cliente deseje viajar em um voo que não está sendo oferecido pela Ambrosino Airlines.

Caso exista disponibilidade no voo, imprima o número do documento de identidade do cliente. Caso não exista disponibilidade ou não exista o voo desejado, imprima a string: INDISPONIVEL

Lembre-se que uma vez que o cliente faz a reserva em um voo, a disponibilidade deve ser reduzida.
'''
count = 1
voos = {}
while count <= 37:
    temp = map(int, raw_input().split())
    voos[temp[0]] = temp[1]
    count += 1
while True:
    entrada = raw_input()
    if entrada == '9999':
        break
    id, pedido = map(int, entrada.split())
    if voos.has_key(pedido):
        if voos[pedido] >= 1:
            print id
            voos[pedido] -= 1
        else:
            print 'INDISPONIVEL'
    else:
        print 'INDISPONIVEL'