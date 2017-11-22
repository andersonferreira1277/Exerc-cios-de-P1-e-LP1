#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Vov� Jo�o tem uma banca de jornais; ele tem muitos clientes, e diariamente recebe muito dinheiro, mas tamb�m faz muitos pagamentos para manter o seu estoque de jornais e revistas. Todo dia ele vai ao banco realizar um dep�sito ou uma retirada de dinheiro. Em alguns dias, o saldo de sua conta no banco fica negativo, mas Vov� Jo�o tem um acordo com o banco que garante que ele somente � cobrado se o saldo for menor do que um valor pr�-estabelecido.
Dada a movimenta��o di�ria da conta do banco do Vov� Jo�o, voc� deve escrever um programa que calcule o menor saldo da conta, no per�odo dado.

Formato de entrada
A primeira linha da entrada cont�m dois n�meros inteiros N e S que indicam respectivamente o n�mero de dias do per�odo de interesse e o saldo da conta no in�cio do per�odo. Cada uma das N linhas seguintes cont�m um n�mero inteiro indicando a movimenta��o de um dia (valor positivo no caso de dep�sito, valor negativo no caso de retirada). A movimenta��o � dada para um per�odo de N dias consecutivos: a primeira das N linhas corresponde ao primeiro dia do per�odo de interesse, a segunda linha corresponde ao segundo dia, e assim por diante.
1 ? N ? 30
-10� ? S ?10�
-10� ? cada movimenta��o ?10�

Formato de sa�da
Seu programa deve imprimir uma �nica linha, contendo um �nico n�mero inteiro, o menor valor de saldo da conta no per�odo dado.
Perceba que voc� deve sempre esperar o final do dia para verificar o saldo. Ou seja, embora o problema informe o saldo inicial, voc� precisa realizar a primeira opera��o para verificar o saldo ao final do dia.
"""
periodo = map(int, raw_input().split())
count = 1
saldo = periodo[1]
saldo_menor = int
while count <= periodo[0]:
    temp = float(input())
    saldo = temp+saldo
    if saldo < saldo_menor:
        saldo_menor = saldo
    count += 1
print ("%d" % saldo_menor)