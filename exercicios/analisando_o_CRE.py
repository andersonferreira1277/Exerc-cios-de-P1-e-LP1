#-*- coding: latin1 -*-
#windows 10 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
"""
Descrição
Fernanda tem um projeto de extensão e precisa selecionar alunos. Escreva um programa para que ela possa informar matrícula e CRE dos vários inscritos, e ver, ao final, a matrícula do aluno com menor CRE e o CRE médio de todos os candidatos.

Formato de entrada
Um String (matrícula) e um float (CRE) para cada candidato.
A entrada de dados deve parar quando for informada a matrícula 999

Formato de saída
Um String com a matrícula que teve o menor CRE, seguida por um float com duas casas decimais para a média de CREs.
Esses valroes devem ser separados por uma quebra de linha (enter)

http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_10.html

http://aprenda-python.blogspot.com.br/2012/12/como-pegar-chave-do-item-de-maior-valor.html
"""
chave = raw_input()
matricula = {}
matricula[chave] = float(input())
while chave != "999":
    chave = raw_input()
    if chave == "999":
        break
    matricula[chave] = float(input())
print min(matricula, key=matricula.get)
print ("%.2f" % (sum(matricula.values())/len(matricula.values())))