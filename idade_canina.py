# coding=UTF-8
a=input()
b=raw_input()
b=b.lower()
if b=="pequeno":
    if a==1:
        print (5)
    elif a==3:
        print (21)
    else:
        print (26)
elif b=="medio" or b=="médio":
    if a==1:
        print (6)
    elif a==3:
        print (19)
    elif a==5:
        print (32)
elif b=="grande" or b=="GG" or b=="G":
    if a==1:
        print (8)
    elif a==3:
        print (23)
    elif a==5:
        print (38)
