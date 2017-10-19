#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Sabe-se que anos bissextos são os anos que possuem 366 dias no calendário, esse dia representa o acrescimo de 1 dia em Fevereiro, que deixa de ter 28 dias, e passa a ter 29

Formato de entrada
Dois inteiros, representando um ano inicial, e um ano final.

Formato de saída
Todos os anos bissextos entre os dois anos dados, inclusive.
Se não houver anos bissextos, imprimir "-1", sem as aspas.
Obs: a saida deve ser seguida de uma quebra de linha.
"""
"""
http://ciencia.hsw.uol.com.br/ano-bissexto1.htm
"""
entrada = raw_input()
entrada = entrada.split()
entrada = map(int, entrada)
resposta = []
for i in range(entrada[0],entrada[1]+1):
    if (i%4 == 0) and ((i%100 != 0) or (i%10 != 0)):
        resposta.append(i)
    elif (i%4 == 0) and (i%400 == 0):
        resposta.append(i)
if resposta == []:
    print ("-1")
else:
    for x in resposta:
        print (x)