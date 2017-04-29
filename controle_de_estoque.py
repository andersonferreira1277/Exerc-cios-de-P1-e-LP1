#-*- coding: latin1 -*-
#kubuntu 16.04 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Em um estoque s�o dados os c�digos das mercadorias e as respectivas quantidades existentes. A seguir, s�o fornecidos os pedidos dos clientes. O seu objetivo  � fazer um programa de controle do estoque que:
Leia o estoque inicial (m�ximo de 100 mercadorias);
Leia os pedidos dos clientes, constitu�do, cada um, de: n�mero do cliente; c�digo da mercadoria e quantidade desejada;
Seja verificado, para cada pedido, se ele pode ser atendido integralmente. Caso possa ser atendido, imprima OK, caso contr�rio ESTOQUE INSUFICIENTE;
Ao final da execu��o do programa, imprima o estoque final;

Uma lista de inteiros n e m, indicando o c�digo da mercadoria e a quantidade dessa mercadoria dispon�vel no estoque, respectivamente.
Essa lista se encerra quando n for igual a 9999.
Depois ser� dada uma lista de inteiros i, j e k, onde i corresponde ao n�mero do cliente, j � o c�digo da mercadoria sendo solicitada e k a quantidade pedida.
Os pedidos se encerram quando i for igual a 9999.

Para cada pedido, a sa�da deve imprimir OK ou ESTOQUE INSUFICIENTE, seguida de um final de linha.
Ao final dos pedidos, deve ser impresso uma lista de inteiros x, y correspondendo ao c�digo e ao estoque restante das mercadorias.
Cada par x, y dever ser impresso em uma linha.
'''
estoque = {}
lista_produtos = [] #lista para auxiliar na impress�o final, pois o dicionarios n�o s�o ordenados.
while True:
    temp = raw_input()
    if temp == '9999':
        break
    estoque[(map(int, temp.split()))[0]] = (map(int, temp.split()))[1]
    lista_produtos.append(map(int, temp.split())[0])
resposta = []
while True: #este looping responde as perguntas... se o produto est� ok ou insuficiente
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