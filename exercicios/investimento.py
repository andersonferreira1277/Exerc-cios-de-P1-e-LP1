#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Uma pessoa aplicou seu capital a juros e deseja saber, trimestralmente, a posi��o de seu investimento C inicial. Chamando de i a taxa de juros do trimestre,
escreva uma tabela que, para cada trimestre, d� o rendimento auferido e o saldo acumulado durante um per�odo de X anos, supondo-se que nenhuma retirada tenha sido feita.

Formato de entrada
Dois n�meros de ponto flutuante separados por espa�o contendo o investimento inicial, a taxa de juros trimestral e um inteiro indicando o per�odo em anos.

Formato de sa�da
Uma tabela, cada linha � escrita na forma:
Rendimento: R Montante: M
onde R e M s�o n�meros de ponto flutuante formatado com duas casas decimais.
"""
"""
https://www.youtube.com/watch?v=B1-TAf7fsPE
"""
a = raw_input()
capital, juros, periodo = a.split()
capital = float(capital)
juros = float(juros)
periodo = int(periodo) # transformei a entrada em variaveis, para ficar mais f�cil de escrever o c�digo
periodo = periodo*12
rendimento = 0
for i in range(1,periodo,3):
    rendimento = capital*juros
    capital = capital*juros + capital
    print ("Rendimento: %.2f Montante: %.2f" % (rendimento,capital))