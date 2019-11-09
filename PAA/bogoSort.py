import numpy as np
import numpy.random
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from random import *


def linear(casosTeste, ordem, tempo):
    casosTestestr = [str(x) for x in casosTeste] # convertendo array int para array str

    x1 = range(len(casosTestestr))

    fig = plt.figure()
    fig.canvas.set_window_title(ordem)
    ax = fig.add_subplot(111)
    # ax.set_ylim(0,10)
    plt.plot(casosTestestr, tempo)
    for i,j in zip(x1,tempo):
        t = "{0:.4f}".format(tempo[i])
        # condição especial para alinhar o tempo junto ao gráfico e não ficar cortando o tempo
        if i == 2:
            i -= 0.3
        ax.annotate(str(t)+"s",xy=(i,j))
    plt.xlabel("N casos de teste")
    plt.ylabel("Número de operações")
    plt.title("Bogo Sort")
    plt.savefig(ordem+' - BogoSort.png')

def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True

def bogo(x):
    operacoes = 0
    while not inorder(x):
        operacoes += 1
        shuffle(x)
    return x, operacoes

k = []
print("Digite 3 qtd's de casos de teste:\n")
k.append(int(input("1º:\n")))
k.append(int(input("2º:\n")))
k.append(int(input("3º:\n")))
# k.append(int(input("4º:\n")))

resultadosTempo = []
resultadosOperacoes = []


for x in k:
    print("Ordem 1 - Crescente\n"+str(x)+" Casos de teste")
    arrayCrescente = list(range(0, x))
    inicio = time.time() # inicio do algoritmo de ordenação
    inicio_stamp = datetime.fromtimestamp(inicio) # Convertendo inicio para uma data legivel

    print("Começando a ordenar: "+inicio_stamp.strftime("%d-%m-%Y %H:%M:%S.%f"))
    array, h = bogo(arrayCrescente)

    fim = time.time()
    fim_stamp = datetime.fromtimestamp(fim) # Convertendo fim para uma data legivel
    print("Finalizado: "+fim_stamp.strftime("%d-%m-%Y %H:%M:%S.%f"))
    print("Duração: "+str(fim - inicio))
    print("Operações: "+str(h))
    resultadosOperacoes.append(h)
    resultadosTempo.append(fim - inicio)

linear(k, "Ordem 1", resultadosTempo)

# array decrescente

resultadosTempo = []
resultadosOperacoes = []


for x in k:
    print("Ordem 2 - decrescente\n"+str(x)+" Casos de teste")
    arraydecrescente = list(range(x, 0, -1)) # de x-1 a 0
    inicio = time.time() # inicio do algoritmo de ordenação
    inicio_stamp = datetime.fromtimestamp(inicio) # Convertendo inicio para uma data legivel

    print("Começando a ordenar: "+inicio_stamp.strftime("%d-%m-%Y %H:%M:%S.%f"))
    array, h = bogo(arraydecrescente)

    fim = time.time()
    fim_stamp = datetime.fromtimestamp(fim) # Convertendo fim para uma data legivel
    print("Finalizado: "+fim_stamp.strftime("%d-%m-%Y %H:%M:%S.%f"))
    print("Duração: "+str(fim - inicio))
    print("Operações: "+str(h))
    resultadosOperacoes.append(h)
    resultadosTempo.append(fim - inicio)

linear(k, "Ordem 2", resultadosTempo)


# array aleatorio

resultadosTempo = []
resultadosOperacoes = []


for x in k:
    print("Ordem 3 - aleatorio\n"+str(x)+" Casos de teste")
    arrAleatorio = np.random.randint(0, x, x) # criando o array aleatorio
    inicio = time.time() # inicio do algoritmo de ordenação
    inicio_stamp = datetime.fromtimestamp(inicio) # Convertendo inicio para uma data legivel

    print("Começando a ordenar: "+inicio_stamp.strftime("%d-%m-%Y %H:%M:%S.%f"))
    array, h = bogo(arrAleatorio)

    fim = time.time()
    fim_stamp = datetime.fromtimestamp(fim) # Convertendo fim para uma data legivel
    print("Finalizado: "+fim_stamp.strftime("%d-%m-%Y %H:%M:%S.%f"))
    print("Duração: "+str(fim - inicio))
    print("Operações: "+str(h))
    resultadosOperacoes.append(h)
    resultadosTempo.append(fim - inicio)

linear(k, "Ordem 3", resultadosTempo)
