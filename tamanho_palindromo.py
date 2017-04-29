#-*- coding: latin1 -*-
#kubuntu 64 bits
#python 2.7.12
#Feito por andersonferreira1277@gmail.com
from unicodedata import normalize
palavra = raw_input().lower()
palavra = normalize('NFKD', palavra.decode('latin1')).encode('ASCII','ignore')
if palavra == palavra[::-1]:
    print 'SIM' 
    print len(palavra)/2
else:
    print 'NAO'