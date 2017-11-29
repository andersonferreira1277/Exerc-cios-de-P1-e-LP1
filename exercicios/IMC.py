peso = float(input("Digite o peso:\n"))
altura = float(input("Digite a altura: - ex: 1.68\n"))
altura = altura**2
r = peso/altura
if r<18.5:
    print("%.2f MAGREZA" % r)
elif r>=18.5 and r<=24.9:
    print("%.2f SAUDAVEL" % r)
elif r>=25 and r<=29.9:
    print("%.2f SOBREPESO" % r)
elif r>30:
    print("%.2f OBESIDADE" % r)
else:
    print("invalido")
