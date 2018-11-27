# -*- encoding: utf-8 -*-
from datetime import date, datetime
import ipdb

def datasLimites(dataBase, retroagir):
    """@Param dataBase, data a partir da qual irá retroagir"""
    """@Param retroagir, Quantidade de meses para retroagir"""
    datasResultado = []
    dataBase2 = dataBase
    for i in range(retroagir):
        # ipdb.set_trace()
        dataBase2 = datetime(dataBase2.year, dataBase2.month, 1) # primeiro dia da data base
        dataBase2 = date.fromordinal(dataBase2.toordinal()-1) # mês anterior
        datasResultado.append(dataBase2.strftime("%Y%m%d"))
        
    datasResultado.reverse() # invertendo lista
    for k in datasResultado:
        print(k)

datasLimites(datetime.now(), 9)