#-*- coding: latin1 -*-
#kubuntu 16.04 64bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
O senhor Huxley, amigo do Ambrósio, escreveu um texto em um pedaço de papel e quer saber quantos buracos existem no texto. Mas o que é um buraco? Imagine, por exemplo, que as letras "A", "D", "O", "P", "R" possuem apenas um buraco. Da mesma forma, a letra "B" possui dois buracos. Já as letras "C", "E", "F", "K" não possuem buracos. Nós devemos considerar que o número de buracos em um texto é igual ao número total de buracos nas letras do texto. Ajude o sr. Huxley a determinar quantos buracos existem no texto.

A primeira linha contém um inteiro simples T <= 40 que indica o número de casos de testes. Depois, seguem-se T casos de teste. Cada linha do caso de teste contém um texto não vazio composto somente de caracteres maiúsculos do alfabeto inglês. O tamanho de cada texto é menor ou igual a 100. Não existem espaços na entrada.

Para cada caso de teste, a saída consiste de uma linha contendo o número de buracos encontrado no caso de teste.
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