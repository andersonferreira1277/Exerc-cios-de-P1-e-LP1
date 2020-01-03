"""
Transforma:
121212
656566
565656

EM:
('121212', '656566', '565656')


"""
with open('lista.txt') as f:
    lines = f.readlines()

linhasSemEspaco = []
for x in lines:
    linhasSemEspaco.append(x.strip())

placeholders = ', '.join("'"+unused+"'" for unused in linhasSemEspaco)
query= '(%s)' % placeholders
print(query)
g = open("resultado.txt", "a")
g.write(query)
g.close()
