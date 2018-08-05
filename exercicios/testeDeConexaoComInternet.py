#-*- coding: utf-8 -*-
import socket, datetime
confiaveis = ['www.google.com', 'www.uol.com.br', 'www.globo.com.br']


def check_host(confiaveis):
	for host in confiaveis:
		a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		a.settimeout(.5)
		try:
			b = a.connect_ex((host, 80))
			if b == 0:
				print("Conectou a: "+host)
				print("Hora: "+datetime.datetime.now().strftime("%T"))
		except:
			print("Não conectou a: "+host)
	a.close()

if __name__ == '__main__':
	check_host(confiaveis)