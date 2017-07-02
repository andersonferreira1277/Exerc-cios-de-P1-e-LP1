#-*- coding: latin1-*-
import socket
class Verificar:
    def __init__(self):
        pass
    def teste(self):
        try:
            socket.gethostbyname('www.google.com.br')
        except:
            return 'Sem internet'
        return 'Conectado'