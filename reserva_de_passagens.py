#-*- coding: latin1 -*-
#kubuntu 16.04 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
O cen�rio � uma terra muito distante, onde ainda ocorre o caos a�reo. Voc�, � o desenvolvedor de software respons�vel pelos sistemas da Ambrosino Airlines. Sua miss�o � desenvolver um sistema de reserva de passagens. A Ambrosino Airlines possui 37 voos fixos.

Uma sequ�ncia de 37 pares de inteiros, indicando o n�mero do voo e a quantidade de lugares dispon�veis no respectivo voo. Depois voc� ler� uma sequ�ncia de pedidos de reserva. Cada pedido de reserva � representado por um par de inteiros indicando, respectivamente, o n�mero do documento de identidade do cliente e o n�mero do voo que o cliente deseja viajar. A entrada se encerra quando o n�mero do documento de identidade do cliente for igual a 9999. Existe a possibilidade de que o cliente deseje viajar em um voo que n�o est� sendo oferecido pela Ambrosino Airlines.

Caso exista disponibilidade no voo, imprima o n�mero do documento de identidade do cliente. Caso n�o exista disponibilidade ou n�o exista o voo desejado, imprima a string: INDISPONIVEL

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