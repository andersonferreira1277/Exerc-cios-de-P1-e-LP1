entrada = raw_input()
r1,r2,r3,r4,r5 = entrada.split()
r1=int(r1)
r2=int(r2)
r3=int(r3)
r4=int(r4)
r5=int(r5)
a = 0
if (r1==1 or r1==0) and (r2==1 or r2==0) and r3==1 and r4==1 and (r5==1 or r5==0):
    if (r1+r3+r5==3) or (r1+r4+r5==3) or (r2+r3+r5==3) or (r2+r4+r5==3):
        print("AVALIADO\n")
    else:
        print(a)
else:
	print (a)
	