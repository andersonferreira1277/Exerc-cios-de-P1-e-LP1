import numpy as np
import numpy.random
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


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
    plt.title("OddEvenSort - "+ordem)
    plt.savefig(ordem+'OddEvenSort.png')

def oddEvenSort(arr, n): 
    operacoes = 0
    # Initially array is unsorted 
    isSorted = 0
    while isSorted == 0: 
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2): 
            operacoes += 1
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                isSorted = 0
                  
        for i in range(0, n-1, 2): 
            operacoes += 1
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                isSorted = 0
      
    return operacoes

k = []
print("Digite 4 qtd's de casos de teste:\n")
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
    h = oddEvenSort(arrayCrescente, len(arrayCrescente))

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
    h = oddEvenSort(arraydecrescente, len(arraydecrescente))

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
    h = oddEvenSort(arrAleatorio, len(arrAleatorio))

    fim = time.time()
    fim_stamp = datetime.fromtimestamp(fim) # Convertendo fim para uma data legivel
    print("Finalizado: "+fim_stamp.strftime("%d-%m-%Y %H:%M:%S.%f"))
    print("Duração: "+str(fim - inicio))
    print("Operações: "+str(h))
    resultadosOperacoes.append(h)
    resultadosTempo.append(fim - inicio)

linear(k, "Ordem 3", resultadosTempo)

