#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descri��o
Fernanda tem um projeto de extens�o e precisa selecionar alunos. Escreva um programa para que ela possa informar matr�cula e CRE dos v�rios inscritos, e ver, ao final, a matr�cula do aluno com menor CRE e o CRE m�dio de todos os candidatos.

Formato de entrada
Um String (matr�cula) e um float (CRE) para cada candidato.
A entrada de dados deve parar quando for informada a matr�cula 999

Formato de sa�da
Um String com a matr�cula que teve o menor CRE, seguida por um float com duas casas decimais para a m�dia de CREs.
Esses valroes devem ser separados por uma quebra de linha (enter)

http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_10.html

http://aprenda-python.blogspot.com.br/2012/12/como-pegar-chave-do-item-de-maior-valor.html
"""
matricula = []
var = raw_input()
matricula.append(var)
cre = []
cre.append(float(input()))
cre2 = []
var = ""
while matricula != "999":
    var = raw_input()
    if var == "999":
        break
    matricula.append(var)
    cre.append(float(input()))
for i in cre:
    cre2.append(i)
cre2.sort()
indice = cre.index(cre2[0])
print matricula[indice]
print ("%.2f" % ((sum(cre))/len(cre)))