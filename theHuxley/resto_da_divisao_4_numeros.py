num=input()
a=num/1000
t=num%1000
b=t/100
t=t%100
c=t/10
t=t%10
if t==0 and c==0 and b==0 and a==0:
    print("invalido")
elif t==0 and c==0 and b==0:
    print a
elif t==0 and c==0:
    print("%d%d" % (b,a))
elif t==0:
    print("%d%d%d" % (c,b,a))
else:
    print("%d%d%d%d" % (t,c,b,a))
