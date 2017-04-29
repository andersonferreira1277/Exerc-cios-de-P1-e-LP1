#-*- coding: latin1 -*-
#kubuntu 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Chama-se de quadrado mágico um arranjo, na forma de um quadrado, de N x N números inteiros tal que todas as linhas, colunas e diagonais têm a mesma soma.
Por exemplo, o quadrado abaixo
2 7 6
9 5 1
4 3 8
é um quadrado mágico de soma 15, pois todas as linhas (2 + 7 + 6 = 15, 9 + 5 + 1 = 15 e 4 + 3 + 8 = 15), colunas (2 + 9 + 4 = 15, 7 + 5 + 3 = 15 e 6 + 1 + 8 = 15) e diagonais (2 + 5 + 8 = 15 e 6 + 5 + 4 = 15) têm a mesma soma (15).
Escreva um programa que, dado um quadrado, determine se ele é magico ou não e qual a soma dele (caso seja mágico).

A entrada contém um único conjunto de testes. A primeira linha da entrada de cada caso de teste contém um inteiro N (2 <= N <= 10). As N linhas seguintes contêm N inteiros cada, separados por exatamente um espaço em branco. Os inteiros dentro do quadrado são todos maiores que 0 (zero) e menores ou iguais a 1000.

Seu programa deve imprimir, na saída padrão, uma única linha com um inteiro representando a soma do quadrado mágico ou -1 caso o quadrado não seja mágico.

'''
def quadrado_perfeito(lista):
    primeira = False
    for linhas in lista:
        if primeira == False:
            temp2 = sum(linhas)
            primeira = True
        else:
            if temp2 == sum(linhas):
                temp2 = sum(linhas)
                continue
            else:
                return -1
    soma = 0
    teste = False
    for k in range(len(lista)):
        for x in range(len(lista)):
            soma += lista[x][k]
        if not teste:
            teste = soma
            soma = 0
        else:
            if soma == teste:
                teste = soma
                soma = 0
                continue
            else:
                return -1
    d_soma = 0
    c = 0
    for d in lista:
        d_soma += d[c]
        c += 1
    t = len(lista)-1
    d_soman = 0
    for e in lista:
        d_soman += e[t]
        t -= 1
    if d_soma == temp2 and d_soman == temp2:
        pass
    else:
        return -1


    return temp2

entrada = int(input())
count = 1
lista = []
while count <= entrada:
    temp = map(int, raw_input().split())
    lista.append(temp)
    count += 1
print (quadrado_perfeito(lista))