#!/usr/bin/env python3
"""https://pt.stackoverflow.com/questions/143552/entendendo-o-conceito-de-threads-na-pr%C3%A1tica-em-python"""

from threading import Thread
import time


def carrinho(velocidade,nome):
    distancia = 0
    while distancia <= 1000:
        print("Carrinho :",nome,distancia)
        distancia += velocidade
        time.sleep(velocidade)



carrinho1 = Thread(target=carrinho,args=[1.1,"Ed"])
carrinho2 = Thread(target=carrinho,args=[3.2,"Paulo"])


carrinho1.start()
carrinho2.start()