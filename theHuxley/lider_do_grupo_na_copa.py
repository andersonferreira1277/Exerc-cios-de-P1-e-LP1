#-*- coding: latin1 -*-
#windows 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Descrição
Na Copa do Mundo, os times são organizados em grupos que disputam as vagas para a próxima fase. Para definir qual time será o líder do grupo, primeiro analisa-se a quantidade de pontos. Em caso de empate, o próximo critério é o saldo de gols. Se mesmo assim não for possível definir, são considerados os gols feitos.
Escreva um programa que receba como entrada o nome e essas três informações de dois times, e exiba o nome do time vencedor do grupo (em letras minúsculas). Caso nenhum dos critérios seja capaz de definir o vencedor, o programa deverá exibir a mensagem EMPATE (em maiúsculas).

Formato de entrada
A entrada consiste em 8 valores, sendo um String, seguido por três inteiros, para um time, e depois o mesmo para o outro

Formato de saída
Um String em minúsculas com o nome do time vencedor, ou um String em maiúsculas com a palavra EMPATE.
'''
def contar(matrix):
    if matrix[0][0] > matrix[1][0]:
        return time_1
    if matrix[1][0] > matrix[0][0]:
        return time_2
    if matrix[0][1] > matrix[1][1]:
        return time_1
    if matrix[1][1] > matrix[0][1]:
        return time_2
    if matrix[0][2] > matrix[1][2]:
       return time_1
    if matrix[1][2] > matrix[0][2]:
        return time_2
    else:
        return 'EMPATE'
matrix = [[0,0,0],[0,0,0]]
time_1 = raw_input().lower()
matrix[0][0] = int(input())
matrix[0][1] = int(input())
matrix[0][2] = int(input())
time_2 = raw_input().lower()
matrix[1][0] = int(input())
matrix[1][1] = int(input())
matrix[1][2] = int(input())
print contar(matrix)