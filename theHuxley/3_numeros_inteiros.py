a = input("Digite o primeiro valor")
b = input("Digite o segundo valor")
c = input("Digite o terceiro valor")
#verificar se A é o maior
if a >= b and a >= c:
    if b > c:
        print(c)
        print(b)
        print(a)
    else:
        print(b)
        print(c)
        print(a)
#verificar se B é o maior
elif b >= a and b >= c:
    if a > c:
        print(c)
        print(a)
        print(b)
    else:
        print(a)
        print(c)
        print(b)
#verificar se C é o maior
elif c >= a and c >= b:
    if a > b:
        print(b)
        print(a)
        print(c)
    else:
        print(a)
        print(b)
        print(c)
