#-*- coding: latin1-*-
from unicodedata import normalize
string = '���'
print string
print normalize('NFKD', string.decode('latin1')).encode('ASCII','ignore')
