entrada = raw_input()
r1,r2,r3,r4,r5 = entrada.split()
r1=int(r1)
r2=int(r2)
r3=int(r3)
r4=int(r4)
r5=int(r5)
if (r1==1 or r1==0) and (r2==1 or r2==0) and (r3==1 or r3==0) and  (r4==1 or r4==0) and (r5==1 or r5==0):
    if r1+r2>=1:
        r1=1
    if r3+r4>=1:
        r2=1
    if r1+r2+r5==3:
        print("AVALIADO\n")
    else:
        print("0\n")
