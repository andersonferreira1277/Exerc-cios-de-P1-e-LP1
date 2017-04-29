import random
n = int(input())
m = int(input())
count = 1
while count <= m:
    print ('%d %d %d'% ((random.randint(1,n)),(random.randint(1,n)),(random.randint(0,100))))
    count +=1