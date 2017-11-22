#-*- coding: latin1 -*-
#kubuntu 16.04 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Para Jimmy a banda perfeita tem quatro integrantes, ele e mais tr�s: um baterista, um baixista e um cantor, ele reuniu todos os �lbuns que encontrou na internet e, ap�s escut�-los diversas vezes, compilou o que ele chama de lista de entrosamento entre m�sicos.
Nessa lista ele atribui, para cada par de m�sicos que j� tocaram juntos, uma nota inteira de 1 a 100, que � uma medida de qu�o bem os m�sicos tocam juntos (o n�vel de entrosamento entre eles). Se dois m�sicos nunca tocaram juntos o n�vel de entrosamento � zero. Jimmy nunca tocou com nenhum m�sico da lista. Jimmy quer escolher os outros tr�s m�sicos de tal forma que a soma dos n�veis de entrosamento dos integrantes da banda seja a maior poss�vel.
Mas a lista de entrosamento entre m�sicos ficou muito grande e Jimmy n�o est� conseguindo escolher os integrantes. Por isso, Jimmy est� pedindo sua ajuda! Voc� deve ajudar Jimmy a montar a melhor banda poss�vel fazendo um programa que receba uma lista contendo o n�vel de entrosamento para cada par de m�sicos que j� tocaram junto, e determine os m�sicos que formariam a melhor banda.

Formato de entrada
A primeira linha da entrada � formada por dois inteiros N e M, informando respectivamente o n�mero de m�sicos (3 < N < 100) e o n�mero de pares de m�sicos que j� tocaram juntos (0 < M < 10000). Os m�sicos s�o identificados por n�meros inteiros de 1 a N.
Cada uma das M linhas seguintes cont�m tr�s inteiros X, Y e Z, em que X e Y representa um par de m�sicos (1 < X < N, 1 < Y < N e X != Y ) e Z representa o seu n�vel de entrosamento (1 < Z < 100).
Cada par de m�sicos que j� tocou junto aparece uma �nica vez na entrada.
A Entrada Termina quando (N = M = 0)

Para cada caso de teste a sa�da deve conter tr�s n�meros inteiros em ordem crescente ,separados por espa�o em branco, identificando os tr�s outros m�sicos que devem compor a banda, seguido por um final de linha, caso existam mais deu um trio com a melhor pontua��o, imprima aquele que aparece primeiro na ordem lexicogr�fica
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