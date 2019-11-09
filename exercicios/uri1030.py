nc = int(input()) # Caso de testes
casosDeTeste = []
for i in range(nc):
    entrada = input()
    casosDeTeste.append(entrada)

for x in casosDeTeste:
    case = str(casosDeTeste.index(x)+1)
    tamanhoAnel = int(x.split()[0])
    anel  = list(range(1, tamanhoAnel+1))
    salto = int(x.split()[1])
    indice = 0
    while(len(anel) > 1):
        indice += salto
        indice -=1
        if indice >= len(anel):
            indice = indice%len(anel)
            anel.pop(indice)
        else:
            anel.pop(indice)

    print("Case "+case+": "+str(anel[0]))