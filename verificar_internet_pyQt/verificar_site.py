#-*- coding: UTF-8-*-
"Feito por Anderson Ferreira C�mara - andersonferreira1277@gmail.com"
from os import system as system_call
def ping(host):
    parameters = "-n 2"
    return system_call("ping " + parameters + " " + host) == 0

while (ping("www.professus.com.br")==False):
    print("Sem conexao com o professus")
print("conectado")
