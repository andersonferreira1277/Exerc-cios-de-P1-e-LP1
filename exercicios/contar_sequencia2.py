num = []
for x in range(10):
    num.append(raw_input())
b = num[-1]
c = num.count(b)
print("O numero %s apareceu %s vezes" % (b,c))
