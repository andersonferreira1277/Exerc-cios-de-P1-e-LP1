#-*- coding: latin1 -*-
#kubuntu 16.04 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Para Jimmy a banda perfeita tem quatro integrantes, ele e mais três: um baterista, um baixista e um cantor, ele reuniu todos os álbuns que encontrou na internet e, após escutá-los diversas vezes, compilou o que ele chama de lista de entrosamento entre músicos.
Nessa lista ele atribui, para cada par de músicos que já tocaram juntos, uma nota inteira de 1 a 100, que é uma medida de quão bem os músicos tocam juntos (o nível de entrosamento entre eles). Se dois músicos nunca tocaram juntos o nível de entrosamento é zero. Jimmy nunca tocou com nenhum músico da lista. Jimmy quer escolher os outros três músicos de tal forma que a soma dos níveis de entrosamento dos integrantes da banda seja a maior possível.
Mas a lista de entrosamento entre músicos ficou muito grande e Jimmy não está conseguindo escolher os integrantes. Por isso, Jimmy está pedindo sua ajuda! Você deve ajudar Jimmy a montar a melhor banda possível fazendo um programa que receba uma lista contendo o nível de entrosamento para cada par de músicos que já tocaram junto, e determine os músicos que formariam a melhor banda.

Formato de entrada
A primeira linha da entrada é formada por dois inteiros N e M, informando respectivamente o número de músicos (3 < N < 100) e o número de pares de músicos que já tocaram juntos (0 < M < 10000). Os músicos são identificados por números inteiros de 1 a N.
Cada uma das M linhas seguintes contém três inteiros X, Y e Z, em que X e Y representa um par de músicos (1 < X < N, 1 < Y < N e X != Y ) e Z representa o seu nível de entrosamento (1 < Z < 100).
Cada par de músicos que já tocou junto aparece uma única vez na entrada.
A Entrada Termina quando (N = M = 0)

Para cada caso de teste a saída deve conter três números inteiros em ordem crescente ,separados por espaço em branco, identificando os três outros músicos que devem compor a banda, seguido por um final de linha, caso existam mais deu um trio com a melhor pontuação, imprima aquele que aparece primeiro na ordem lexicográfica
'''
dicio = {}
while True:
    temp = raw_input()
    if temp == '0 0':
        break
    musicos, pares = map(int, temp.split())
    for i in range(1,musicos+1):
        dicio[i] = 0
    count = 1
    nota = []
    while count <= pares:
        nota.append(map(int, raw_input().split()))
        count += 1
    entrosamento = [0, 0, 0, 0]
    for i in range(1,musicos+1):
        for x in range(2,musicos+1):
            for k in range(3,musicos+1):
                nota_trio = 0
                for teste in nota:
                    if (teste[0] == i) and (teste[1] == x) or (teste[0] == i) and (teste[1] == k):
                        nota_trio += teste[2]
                    elif (teste[0] == x) and (teste[1] == i) or (teste[0] == x) and (teste[1] == k):
                        nota_trio += teste[2]
                    elif (teste[0] == k) and (teste[1] == i) or (teste[0] == k) and (teste[1] == x):
                        nota_trio += teste[2]
                if nota_trio > entrosamento[3]:
                    entrosamento = [i,x,k,nota_trio]

    lista = entrosamento[0:3]
    lista.sort()
    print ('%d %d %d' % (lista[0],lista[1], lista[2]))