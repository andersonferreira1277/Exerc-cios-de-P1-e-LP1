#-*- conding: latin1-*-
paises, modalidades = map(int, raw_input().split())
resultados = []
for i in range(modalidades):
    temp = map(int, raw_input().split())
    resultados.append(temp)
dados = {}
for i in range(1,paises+1):
    dados[i] = [0,0,0]
for x in range(len(resultados[0])):
    for i in range(len(resultados)):
        add = resultados[i][x]
        dados[add][x] = dados[add][x] + 1
imprmir = sorted(dados, key=dados.get, reverse=True)
for i in imprmir:
    print i
