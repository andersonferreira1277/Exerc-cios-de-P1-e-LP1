#-*- coding: latin1-*-
import socket, time, os
def verificar():
    try:
        socket.gethostbyname('www.google.com.br')
    except:
        print 'N�o est� conectado a internet.'
        time.sleep(5)
        verificar()
    return 'Conectado.'
print verificar()
os.system('pause')
