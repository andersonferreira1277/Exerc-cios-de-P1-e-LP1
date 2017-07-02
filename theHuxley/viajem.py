pipa2,pipa3,pipa_passeo = 600,900,75
fortaleza3,fortaleza4,fortaleza_passeo = 950,1120,60
grupo = float(input())
cidade = raw_input()
quartos = int(input())
cidade = cidade.lower()
if cidade=="pipa":
    if quartos==3:
        r_total = pipa3+(pipa_passeo*grupo)
        r_pessoa = r_total/grupo
        print("%.2f" % r_total)
        print("%.2f" % r_pessoa)
    elif quartos==2:    
        r_total = pipa2+(pipa_passeo*grupo)
        r_pessoa = r_total/grupo
        print("%.2f" % r_total)
        print("%.2f" % r_pessoa)
elif cidade=="fortaleza":
    if quartos==3:
        r_total = fortaleza3+(fortaleza_passeo*grupo)
        r_pessoa = r_total/grupo
        print("%.2f" % r_total)
        print("%.2f" % r_pessoa)
    elif quartos==4:
        r_total = fortaleza4+(fortaleza_passeo*grupo)
        r_pessoa = r_total/grupo
        print("%.2f" % r_total)
        print("%.2f" % r_pessoa)
else:
    print("invalido")
