#-*- coding: latin1 -*-
#kubuntu 16.04 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
O senhor Huxley, amigo do Ambr�sio, escreveu um texto em um peda�o de papel e quer saber quantos buracos existem no texto. Mas o que � um buraco? Imagine, por exemplo, que as letras "A", "D", "O", "P", "R" possuem apenas um buraco. Da mesma forma, a letra "B" possui dois buracos. J� as letras "C", "E", "F", "K" n�o possuem buracos. N�s devemos considerar que o n�mero de buracos em um texto � igual ao n�mero total de buracos nas letras do texto. Ajude o sr. Huxley a determinar quantos buracos existem no texto.

A primeira linha cont�m um inteiro simples T <= 40 que indica o n�mero de casos de testes. Depois, seguem-se T casos de teste. Cada linha do caso de teste cont�m um texto n�o vazio composto somente de caracteres mai�sculos do alfabeto ingl�s. O tamanho de cada texto � menor ou igual a 100. N�o existem espa�os na entrada.

Para cada caso de teste, a sa�da consiste de uma linha contendo o n�mero de buracos encontrado no caso de teste.
'''
def contar_buracos(lista_strings):
    for i in lista_strings:
        buracos = 0
        for x in i:
            if (x == 'A') or (x == 'D') or (x == 'O') or (x == 'P') or (x == 'R'):
                buracos += 1
            elif (x == 'B'):
                buracos += 2
            else:
                continue
        print buracos
linhas = int(input())
count = 1
lista_strings = []
while count <= linhas:
    string = raw_input()
    lista_strings.append(string)
    count +=1
contar_buracos(lista_strings)