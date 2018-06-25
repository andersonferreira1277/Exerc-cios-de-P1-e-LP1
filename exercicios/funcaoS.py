So = float(input("Digite So\n"))
v = float(input("Digite v\n"))

t = 4

x = So + v * t
t = 8
y = So + v * t

z = (80-So)/v

print("A posição do carro no instante 4s é igual a {:.2f}".format(x))
print("O espaço percorrido pelo carro após 8s é igual a {:.2f}".format(y))
print("instante em que o carro passa pela posição 80m é igual a {:.2f}".format(z))