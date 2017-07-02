# -*- coding: latin1 -*-
# windows 10 64 bits
# python 2.7.12
# Feito por andersonferreira1277@gmail.com
"""
Descrição
Um professor de Português estava corrigindo resumos de textos que seus alunos fizeram, porém, encontrou uma falha grave em todos os textos.
No início das frases e após os pontos finais, a primeira letra estava escrita em letra minúscula.
Ao questionar seus alunos, descobriu que era um erro do editor de texto que todos usaram.
Como ele é muito seu amigo, e você ficou sabendo desse problema que ele enfrentava então se ofecereu para criar um algoritmo para corrigir esse erro.
Crie um programa que troque os caracteres de inicio de frase e após ponto final em minúsculo para maiúsculo.

Formato de entrada
Você receberá um inteiro, indicando quantas linha terá o texto, e o texto, em forma de array de caracteres bidimensional.

Formato de saída
O texto, na mesma ordem que veio na entrada, corrigido de acordo com a regra de letra maiúscula no inicio de frase e após ponto final.
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