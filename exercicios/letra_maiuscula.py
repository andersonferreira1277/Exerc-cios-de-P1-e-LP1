# -*- coding: latin1 -*-
# windows 10 64 bits
# python 2.7.12
# Feito por andersonferreira1277@gmail.com
"""
Descri��o
Um professor de Portugu�s estava corrigindo resumos de textos que seus alunos fizeram, por�m, encontrou uma falha grave em todos os textos.
No in�cio das frases e ap�s os pontos finais, a primeira letra estava escrita em letra min�scula.
Ao questionar seus alunos, descobriu que era um erro do editor de texto que todos usaram.
Como ele � muito seu amigo, e voc� ficou sabendo desse problema que ele enfrentava ent�o se ofecereu para criar um algoritmo para corrigir esse erro.
Crie um programa que troque os caracteres de inicio de frase e ap�s ponto final em min�sculo para mai�sculo.

Formato de entrada
Voc� receber� um inteiro, indicando quantas linha ter� o texto, e o texto, em forma de array de caracteres bidimensional.

Formato de sa�da
O texto, na mesma ordem que veio na entrada, corrigido de acordo com a regra de letra mai�scula no inicio de frase e ap�s ponto final.
Com uma quebra de linha ao fim.
"""
limite = int(input())
count = 1
resultado = ""
while count <= limite:
    frase = raw_input()
    if len(frase.split(". ")) == 1:
        print frase.capitalize()
    else:
        frase = frase.split(". ")
        for i in frase:
            if frase.index(i) < len(frase)-1:
                resultado = resultado + i.capitalize()+". "
            else:
                resultado = resultado + i.capitalize()
        print resultado
    count += 1