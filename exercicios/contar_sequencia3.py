num = raw_input()
num = map(int, num.split())
b = num[-1]
c = num.count(b)
print("O numero %s apareceu %s vezes" % (b,c))
