#-*- coding: latin1 -*-
#kubuntu 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
'''
Faça um programa para corrigir provas de múltipla escolha. Cada prova tem 10 questões, cada questão valendo um ponto. O primeiro conjunto de dados a ser lido é o gabarito para a correção da prova. Depois serão dados os números dos alunos e suas respectivas respostas. O programa encerra a entrada quando o número de um aluno dado for igual a 9999

Uma sequência de 10 caracteres correspondendo ao gabarito. Depois é dada uma sequência de números inteiros representando o aluno e a uma sequencia de caracteres correspondendo a sua resposta.

Para cada aluno lido, na mesma ordem de leitura, deve ser impresso seu número e sua nota. A nota deve ser formatada com uma casa decimal.
Ao final, deve ser impresso a porcentagem de aprovação, sabendo-se que a nota mínima para aprovação é de 6. O percentual deve ser impresso com uma casa decimal seguido do caractere %.
Por fim, deve ser impressa a nota que teve a maior frequência absoluta, ou seja, a nota que apareceu o maior número de vezes (supondo a inexistência de empates).
'''
def corrigir(provas):
	for i in range(len(provas)):
		count = 0.0
		escolhas = provas[i][1]
		for k in range(len(escolhas)):
			if escolhas[k] == gabarito[k]:
				count += 1.0
		if count >= 6.0:
			lista_aprovados.append(count)
		lista_resultados.append(count)
		print ('%s %.1f' % (provas[i][0],count))
		
def contar(lista):
	global fre
	count_l = 1
	for i in lista:
		if count_l < lista.count(i):
			count_l = lista.count(i)
			fre = i
	return fre
	
	
gabarito = raw_input()
provas	= []
while True:
	temp = raw_input().split()
	if temp[0] == '9999' or temp[1] == '9999':
		break
	provas.append(temp)
lista_aprovados = []
lista_resultados = []
corrigir(provas)
print ('%.1f%%' % ((len(lista_aprovados)*100.0)/len(provas)))
fre = lista_resultados[0]
print ('%.1f' % (contar(lista_resultados)))
