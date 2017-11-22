num = []
for x in range(10):
    num.append(int(input()))
b = num[-1]
c = num.count(b)
print("O numero %d apareceu %d vezes" % (b,c))
