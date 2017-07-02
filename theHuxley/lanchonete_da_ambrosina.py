#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Ambrosina é de lua. Quase todo dia ela quer mudar o cardápio de sua lanchonete. Ambrósio, o programador do sistema, não agüenta mais alterar o código do programa todas as vezes que Ambrosina muda o humor. Então Ambrósio resolveu mudar o software de forma que Ambrosina possa cadastrar o cardápio todas as manhãs, ao iniciar o software.
O software lê a quantidade de produtos a serem cadastrados, e depois o código de LED instalada na lanchonete seguidos pela descrição e preço do produto. Os clientes escolhem os produtos pelo código.
Se o cliente pede um produto não cadastrado ou uma quantidade negativa o pedido é considerado inválido.
O sistema calcula quantos itens o cliente escolheu de cada código e imprime o total da conta, sem descontos! Eita Ambrosina sovina !!

Formato de entrada
Consiste de um inteiro n, representando o número de produtos a serem cadastrados.
Depois, segue o cadastro dos n produtos, onde serão lidos para cada produto:
um inteiro representando o código de LED,
uma descrição do produto
e um número real representando o preço.
Depois, são lidos os pedidos.
O pedido consiste do código do produto e da quantidade de itens daquele produto que será pedido. O pedido se encerra quando o código lido é igual a 0.

Formato de saída
O valor que o cliente deve pagar, formatado com duas casas decimais. Pedidos inválidos são ignorados.
"""
#=============================cadastro======================================
lista = {} #Dicionario de códigos e produtos
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