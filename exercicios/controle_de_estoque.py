#-*- coding: latin1 -*-
#kubuntu 16.04 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Em um estoque são dados os códigos das mercadorias e as respectivas quantidades existentes. A seguir, são fornecidos os pedidos dos clientes. O seu objetivo  é fazer um programa de controle do estoque que:
Leia o estoque inicial (máximo de 100 mercadorias);
Leia os pedidos dos clientes, constituído, cada um, de: número do cliente; código da mercadoria e quantidade desejada;
Seja verificado, para cada pedido, se ele pode ser atendido integralmente. Caso possa ser atendido, imprima OK, caso contrário ESTOQUE INSUFICIENTE;
Ao final da execução do programa, imprima o estoque final;

Uma lista de inteiros n e m, indicando o código da mercadoria e a quantidade dessa mercadoria disponível no estoque, respectivamente.
Essa lista se encerra quando n for igual a 9999.
Depois será dada uma lista de inteiros i, j e k, onde i corresponde ao número do cliente, j é o código da mercadoria sendo solicitada e k a quantidade pedida.
Os pedidos se encerram quando i for igual a 9999.

Para cada pedido, a saída deve imprimir OK ou ESTOQUE INSUFICIENTE, seguida de um final de linha.
Ao final dos pedidos, deve ser impresso uma lista de inteiros x, y correspondendo ao código e ao estoque restante das mercadorias.
Cada par x, y dever ser impresso em uma linha.
'''
estoque = {}
lista_produtos = [] #lista para auxiliar na impressão final, pois o dicionarios não são ordenados.
while True:
    temp = raw_input()
    if temp == '9999':
        break
    estoque[(map(int, temp.split()))[0]] = (map(int, temp.split()))[1]
    lista_produtos.append(map(int, temp.split())[0])
resposta = []
while True: #este looping responde as perguntas... se o produto está ok ou insuficiente
    temp = raw_input()
    if temp == '9999':
        break
    else:
        numero_cliente, produto, pedido = map(int, temp.split())
        if pedido <= estoque[produto]:
            resposta.append('OK')
            estoque[produto] -= pedido
        else:
            resposta.append('ESTOQUE INSUFICIENTE')
for i in resposta:
    print i
for i in lista_produtos:
    print ('%d %d' % (i,estoque[i]))