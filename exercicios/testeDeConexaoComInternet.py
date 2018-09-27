# -*- coding: utf-8 -*-
import socket, datetime, time, csv
confiaveis = ['www.google.com', 'www.uol.com.br', 'www.globo.com']


def check_host(confiaveis):

    while True:

        for host in confiaveis:
            a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            a.settimeout(.5)
            try:
                b = a.connect_ex((host, 80))
                if b == 0:
                    s = "Conectou a: " + host
                    s = s + " - Data e hora: " + datetime.datetime.now().strftime("%Y-%m-%d %T")
                else:
                    s = "Não conectou a: " + host
                    s = s + " - Data e hora: " + datetime.datetime.now().strftime("%Y-%m-%d %T")
            except:
                s = "Não conectou a: " + host
                s = s + " - Data e hora: " + datetime.datetime.now().strftime("%Y-%m-%d %T")
            a.close()
            with open("relatorioInternet.txt", 'a') as arquivo:
                arquivo.write(s)
                arquivo.write("\n")
                print(s)
        time.sleep(60*30) # tempo em segundos


if __name__ == '__main__':

    check_host(confiaveis)