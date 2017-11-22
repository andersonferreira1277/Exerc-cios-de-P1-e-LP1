#-*- coding: latin1 -*-
#windows 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Escreva um programa que transforme o computador numa urna eletr�nica para elei��o, em segundo turno, para presidente de um pa�s chamado Ambrol�ndia. Nessas elei��es concorrem os candidatos 83-Alibab� e 93-Alcapone. Cada voto deve ser dado pelo n�mero do candidato, permitindo-se ainda o voto 0 para voto em branco. Qualquer voto diferente dos j� citados � considerado nulo. No final da elei��o o programa deve emitir um relat�rio contendo a vota��o de cada candidato, a quantidade votos em branco, a quantidade de votos nulos e o candidato eleito e os respectivos percentuais.
Em Ambrol�ndia, o percentual de votos � calculado considerando os votos v�lidos. O voto nulo n�o � considerado um voto v�lido. Entretanto, o voto em branco � considerado um voto v�lido.

A entrada consiste de um conjunto de n�meros inteiros, um por linha. A elei��o termina quando o n�mero digitado � -1.
O n�mero de inteiros dados � maior que um e menor que cem milh�es.
Considere tamb�m que cada candidato tem pelo menos um voto.

A sa�da consiste de um relat�rio impresso no seguinte formato:
x
y
z
w
k
a
b
Onde, x � quantidade de votos do candidato Alibab�, y a quantidade de votos do candidato Alcapone, z a quantidade de votos em branco, w a quantidade de votos nulos, k � o n�mero 83 ou 93 indicando qual foi o candidato vencedor, a � o percentual de votos do candidato Alibab� e b � o percentual de votos do candidato Alcapone.
O percentual de votos deve ser impresso com duas casas decimais e sem o sinal de porcentagem. Exemplo, para representar trinta e quatro ponto vinte e cinco porcento voc� deve imprimir: 34.25
Considere tamb�m que sempre haver� um candidato vencedor, ou seja, nunca haver� um empate.
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