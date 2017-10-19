n = int(input())
lista = []
for d in range(1,n+1):
    a = (2*(d-1))* (2**d-1)
    lista.append(a)
i = 1
for y in range(1, n):
    if (y == lista[i]):
        print lista[i]
        i = i +1