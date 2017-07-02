#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Vovô João tem uma banca de jornais; ele tem muitos clientes, e diariamente recebe muito dinheiro, mas também faz muitos pagamentos para manter o seu estoque de jornais e revistas. Todo dia ele vai ao banco realizar um depósito ou uma retirada de dinheiro. Em alguns dias, o saldo de sua conta no banco fica negativo, mas Vovô João tem um acordo com o banco que garante que ele somente é cobrado se o saldo for menor do que um valor pré-estabelecido.
Dada a movimentação diária da conta do banco do Vovô João, você deve escrever um programa que calcule o menor saldo da conta, no período dado.

Formato de entrada
A primeira linha da entrada contém dois números inteiros N e S que indicam respectivamente o número de dias do período de interesse e o saldo da conta no início do período. Cada uma das N linhas seguintes contém um número inteiro indicando a movimentação de um dia (valor positivo no caso de depósito, valor negativo no caso de retirada). A movimentação é dada para um período de N dias consecutivos: a primeira das N linhas corresponde ao primeiro dia do período de interesse, a segunda linha corresponde ao segundo dia, e assim por diante.
1 ? N ? 30
-10³ ? S ?10³
-10³ ? cada movimentação ?10³

Formato de saída
Seu programa deve imprimir uma única linha, contendo um único número inteiro, o menor valor de saldo da conta no período dado.
Perceba que você deve sempre esperar o final do dia para verificar o saldo. Ou seja, embora o problema informe o saldo inicial, você precisa realizar a primeira operação para verificar o saldo ao final do dia.
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