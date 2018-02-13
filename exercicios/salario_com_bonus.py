nome = raw_input()
salario = float(input())
bonus = float(input())
bonus = bonus*15/100
salario = salario+bonus
print("TOTAL = R$ %.2f" % salario)
