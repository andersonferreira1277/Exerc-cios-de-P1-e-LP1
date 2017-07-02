#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Considere o seguinte algoritmo para gerar uma sequ�ncia de n�meros. Comece com um inteiro n. Se n for par, divida por 2. Se n for �mpar, multiplique por 3 e some 1. Repita esse processo com o novo valor de n, terminando quando n = 1. Por exemplo, a seguinte sequ�ncia de n�meros ser� gerada quando n � 22:
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
Embora ainda n�o exista uma prova, os matem�ticos acreditam que esse algoritmo sempre termina com n=1, para qualquer inteiro n. Bem, para este problema aqui no Huxley, essa propriedade se mant�m para qualquer inteiro menor que 1.000.000.
Para uma entrada n, o "tamanho do ciclo" de n � a quantidade de n�meros gerados at� o 1 (incluindo o pr�prio 1). No exemplo acima, o "tamanho do ciclo" de 22 � 16.
Dado dois n�meros i e j, determine o m�ximo "tamanho do ciclo" dentre todos os n�meros entre i e j, incluindo tanto i quanto j.

Formato de entrada
A entrada consiste de uma s�rie de pares de inteiros i e j, um par de inteiros por linha. Todos os inteiros ser�o menores que 1.000.000 e maiores que 0.
Perceba que a entrada s� termina quando n�o houveram mais n�meros. Descubra como fazer o seu programa funcionar nesse caso. Cada linguagem tem uma forma diferente de ler enquanto ainda houver entrada a ser lida.

Formato de sa�da
Para cada par de inteiros i e j, imprima i e j na mesma ordem na qual eles aparecem na entrada e ent�o imprima o m�ximo "tamanho de ciclo" encontrado. Esses 3 n�meros devem ser separados por um espa�o, com todos os 3 n�meros em uma linha e sendo uma linha de sa�da para cada linha da entrada.
Veja o arquivo de exemplo para entender melhor o formato da entrada e da sa�da.

http://stackoverflow.com/questions/21235855/how-to-read-user-input-until-eof
"""
import sys
valores = []
temp = ""
while True:
    temp = sys.stdin.readline().split()
    if temp == []:
        break
    else:
        temp = map(int, temp)
        valores.append(temp)
for x in valores:
    primeiro = x[0]
    segundo = x[1]
    if x[1] < x[0]:
        x.sort()
    count = 0
    count_maior = 0
    for i in range(x[0],x[1]+1):
        count = 1
        while i != 1:
            if i%2 == 0:
                i = i/2
            else:
                i = i*3+1
            count += 1
        if count > count_maior:
            count_maior = count
    print ("%d %d %d" % (primeiro,segundo,count_maior))