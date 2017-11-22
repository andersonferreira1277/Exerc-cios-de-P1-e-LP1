#-*- coding: latin1 -*-
#windows 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Descri��o
Na Copa do Mundo, os times s�o organizados em grupos que disputam as vagas para a pr�xima fase. Para definir qual time ser� o l�der do grupo, primeiro analisa-se a quantidade de pontos. Em caso de empate, o pr�ximo crit�rio � o saldo de gols. Se mesmo assim n�o for poss�vel definir, s�o considerados os gols feitos.
Escreva um programa que receba como entrada o nome e essas tr�s informa��es de dois times, e exiba o nome do time vencedor do grupo (em letras min�sculas). Caso nenhum dos crit�rios seja capaz de definir o vencedor, o programa dever� exibir a mensagem EMPATE (em mai�sculas).

Formato de entrada
A entrada consiste em 8 valores, sendo um String, seguido por tr�s inteiros, para um time, e depois o mesmo para o outro

Formato de sa�da
Um String em min�sculas com o nome do time vencedor, ou um String em mai�sculas com a palavra EMPATE.
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