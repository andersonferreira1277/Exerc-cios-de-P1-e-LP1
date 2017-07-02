#-*- coding: latin1 -*-
#windows 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
count = 1
cinema = []
boliche = []
while count <= 7:
    temp = raw_input().lower()
    if temp == 'cinema':
        cinema.append(temp)
    else:
        boliche.append(temp)
    count +=1
if len(boliche) > len(cinema):
    print 'BOLICHE'
else:
    print 'CINEMA'
