a = int(input())
b = int(input())
c = int(input())
if a==b and a==c and b==c:
    print(1)
elif a==b or a==b or b==a or b==c or c==a or c==b:
    print(3)
else:
    print(2)
