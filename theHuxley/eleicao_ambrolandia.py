#-*- coding: latin1 -*-
#windows 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Escreva um programa que transforme o computador numa urna eletrônica para eleição, em segundo turno, para presidente de um país chamado Ambrolândia. Nessas eleições concorrem os candidatos 83-Alibabá e 93-Alcapone. Cada voto deve ser dado pelo número do candidato, permitindo-se ainda o voto 0 para voto em branco. Qualquer voto diferente dos já citados é considerado nulo. No final da eleição o programa deve emitir um relatório contendo a votação de cada candidato, a quantidade votos em branco, a quantidade de votos nulos e o candidato eleito e os respectivos percentuais.
Em Ambrolândia, o percentual de votos é calculado considerando os votos válidos. O voto nulo não é considerado um voto válido. Entretanto, o voto em branco é considerado um voto válido.

A entrada consiste de um conjunto de números inteiros, um por linha. A eleição termina quando o número digitado é -1.
O número de inteiros dados é maior que um e menor que cem milhões.
Considere também que cada candidato tem pelo menos um voto.

A saída consiste de um relatório impresso no seguinte formato:
x
y
z
w
k
a
b
Onde, x é quantidade de votos do candidato Alibabá, y a quantidade de votos do candidato Alcapone, z a quantidade de votos em branco, w a quantidade de votos nulos, k é o número 83 ou 93 indicando qual foi o candidato vencedor, a é o percentual de votos do candidato Alibabá e b é o percentual de votos do candidato Alcapone.
O percentual de votos deve ser impresso com duas casas decimais e sem o sinal de porcentagem. Exemplo, para representar trinta e quatro ponto vinte e cinco porcento você deve imprimir: 34.25
Considere também que sempre haverá um candidato vencedor, ou seja, nunca haverá um empate.
'''
alibaba = 83
alcapone = 93
votos_alibaba = []
votos_alcapone = []
total_votos = []
branco = []
nulos = []
while True:
    temp = int(input())
    if temp == -1:
        break
    elif temp == alibaba or temp == alcapone or temp == 0:
        total_votos.append(temp)
        if temp == alibaba:
            votos_alibaba.append(temp)
        elif temp == alcapone:
            votos_alcapone.append(temp)
        elif temp == 0:
            branco.append(temp)
    else:
        nulos.append(temp)
print len(votos_alibaba)
print len(votos_alcapone)
print len(branco)
print len(nulos)
if len(votos_alcapone) > len(votos_alibaba):
    print alcapone
else:
    print alibaba
validos = len(votos_alibaba)+len(votos_alcapone)+len(branco)
print ('%.2f' % ((len(votos_alibaba)*100.0)/validos))
print ('%.2f' % ((len(votos_alcapone)*100.0)/validos))