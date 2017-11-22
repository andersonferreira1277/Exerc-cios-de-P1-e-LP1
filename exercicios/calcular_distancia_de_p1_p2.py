import math
p1 = raw_input()
p2 = raw_input()
x1,y1=p1.split()
x2,y2=p2.split()
x1=float(x1)
x2=float(x2)
y1=float(y1)
y2=float(y2)
r=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print("%.4f" % r)

