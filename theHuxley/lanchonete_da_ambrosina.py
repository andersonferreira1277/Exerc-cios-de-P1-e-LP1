#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Ambrosina � de lua. Quase todo dia ela quer mudar o card�pio de sua lanchonete. Ambr�sio, o programador do sistema, n�o ag�enta mais alterar o c�digo do programa todas as vezes que Ambrosina muda o humor. Ent�o Ambr�sio resolveu mudar o software de forma que Ambrosina possa cadastrar o card�pio todas as manh�s, ao iniciar o software.
O software l� a quantidade de produtos a serem cadastrados, e depois o c�digo de LED instalada na lanchonete seguidos pela descri��o e pre�o do produto. Os clientes escolhem os produtos pelo c�digo.
Se o cliente pede um produto n�o cadastrado ou uma quantidade negativa o pedido � considerado inv�lido.
O sistema calcula quantos itens o cliente escolheu de cada c�digo e imprime o total da conta, sem descontos! Eita Ambrosina sovina !!

Formato de entrada
Consiste de um inteiro n, representando o n�mero de produtos a serem cadastrados.
Depois, segue o cadastro dos n produtos, onde ser�o lidos para cada produto:
um inteiro representando o c�digo de LED,
uma descri��o do produto
e um n�mero real representando o pre�o.
Depois, s�o lidos os pedidos.
O pedido consiste do c�digo do produto e da quantidade de itens daquele produto que ser� pedido. O pedido se encerra quando o c�digo lido � igual a 0.

Formato de sa�da
O valor que o cliente deve pagar, formatado com duas casas decimais. Pedidos inv�lidos s�o ignorados.
"""
#=============================cadastro======================================
lista = {} #Dicionario de c�digos e produtos
produtos = []
count = input()
total = 0
for i in range(count):
    codigo = int(input())
    produtos.append(raw_input())
    precos = float(input())
    lista[codigo] = precos
#===========================pedido==========================================
count2 = 1
pedido_codigo = []
pedido_quant = []
count3 = 1
count4 = 0
while (count2 != 0) or (count3 != 0):
    count2 = int(input())
    if (count2 == 0):
        break
    count3 = int(input())
    if (count2 in lista) and (count3 > 0):
        pedido_codigo.append(count2)
        pedido_quant.append(count3)
        count4 +=1 # esse contador indica que algum pedido foi valido
    else:
        continue
if (count4 > 0):
    for x in range(len(pedido_codigo)):
        total = total + lista[pedido_codigo[x]]*pedido_quant[x]
print ("%.2f" % total)