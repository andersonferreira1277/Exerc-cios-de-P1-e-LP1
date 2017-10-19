#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Uma pessoa aplicou seu capital a juros e deseja saber, trimestralmente, a posição de seu investimento C inicial. Chamando de i a taxa de juros do trimestre,
escreva uma tabela que, para cada trimestre, dê o rendimento auferido e o saldo acumulado durante um período de X anos, supondo-se que nenhuma retirada tenha sido feita.

Formato de entrada
Dois números de ponto flutuante separados por espaço contendo o investimento inicial, a taxa de juros trimestral e um inteiro indicando o período em anos.

Formato de saída
Uma tabela, cada linha é escrita na forma:
Rendimento: R Montante: M
onde R e M são números de ponto flutuante formatado com duas casas decimais.
"""
"""
https://www.youtube.com/watch?v=B1-TAf7fsPE
"""
a = raw_input()
capital, juros, periodo = a.split()
capital = float(capital)
juros = float(juros)
periodo = int(periodo) # transformei a entrada em variaveis, para ficar mais fácil de escrever o código
periodo = periodo*12
rendimento = 0
for i in range(1,periodo,3):
    rendimento = capital*juros
    capital = capital*juros + capital
    print ("Rendimento: %.2f Montante: %.2f" % (rendimento,capital))