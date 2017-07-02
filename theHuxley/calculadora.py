#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Ambr�sio est� ficando craque em matem�tica e para provar suas habilidades resolveu fazer uma calculadora. A calculadora deve ser capaz de efetuar as 04 opera��es aritm�ticas (adi��o, subtra��o, multiplica��o e divis�o).

Formato de entrada
Consiste de 02 n�meros reais, um em cada linha, seguidos de um caractere representando a opera��o a ser executada. Depois, consiste de uma sequ�ncia de um n�mero real seguido de um caractere, tamb�m um em cada linha. A entrada termina quando o caractere & for lido.
Perceba que sempre o �ltimo n�mero lido deve ser ignorado, pois ele precede o caractere &.

Formato de sa�da
Consiste em uma sequencia de n�meros reais, um em cada linha, representando o resultado da opera��o escolhida. A partir do terceiro n�mero lido, o resultado deve ser obtido utilizando-se o valor da opera��o anterior. Caso a opera��o n�o seja poss�vel, deve ser impresso "operacao nao pode ser realizada". Os n�meros devem ser impressos com 03 casas decimais.
"""
#==============================vari�veis========================================
r = 0
num = []
operacaoes = []
x = 1
#==============================fun��es========================================
def soma(num1,num2):
    soma = num1 + num2
    return soma

def subtracao(num1,num2):
    subtracao = num1 - num2
    return subtracao

def multi(num1,num2):
    multi = num1 * num2
    return multi

def divisao(num1,num2):
    divisao = num1 / num2
    return divisao
#===========================Principal============================================
entrada = raw_input()
while entrada != "&":
    if (entrada != "&") and (entrada != "+") and (entrada != "-") and (entrada != "*") and (entrada != "/"):
        num.append(float(entrada))
    elif (entrada != "&"):
        operacaoes.append(entrada)
    entrada = raw_input()
r = num[0]
for i in operacaoes:
    if (i == "+"):
        r = soma(r, num[x])
        print("%.3f" % r)
    elif (i == "-"):
        r = subtracao(r, num[x])
        print("%.3f" % r)
    elif (i == "*"):
        r = multi(r, num[x])
        print("%.3f" % r)
    elif (i == "/"):
        if (num[x] == 0):
            print("operacao nao pode ser realizada")
        else:
            r = divisao(r, num[x])
            print("%.3f" % r)
    x += 1
