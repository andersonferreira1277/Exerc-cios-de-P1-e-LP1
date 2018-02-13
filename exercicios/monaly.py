num = int(input())
a = int(input())
b = int(input())
lista = []
for i in range(a,b+1):
    if (i % num == b):
        print i
        lista.append(i)
        continue
if lista == []:
    print ("INEXISTENTE")