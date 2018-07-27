#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
from datetime import date, datetime
from calendar import monthrange

def listaDatas(dia, dataDe, dataAte):
    lista = []
    dataI = data1
    dataI = date(dataI.year, data1.month, dia)
    while dataI.toordinal() <= dataAte.toordinal():
        
        ultimoK = monthrange(dataI.year, dataI.month)
        dataI = date(dataI.year, dataI.month, ultimoK[1])
        n = dataI.toordinal()
        n +=1
        dataI = dataI.fromordinal(n)
        ultimoK = monthrange(dataI.year, dataI.month)
        if dia <= ultimoK[1]:
            dataI = date(dataI.year, dataI.month, dia)
        else:
            dataI = date(dataI.year, dataI.month, ultimoK[1])
        if dataI.toordinal() <= dataAte.toordinal():
            ultimoDia = monthrange(dataI.year, dataI.month)
            if  dia <= ultimoDia[1]:
                dataI = date(dataI.year, dataI.month, dia)
            else:
                dataI = date(dataI.year, dataI.month, ultimoDia[1])
            print(dataI)
            lista.append(dataI)
    return lista

            
if __name__ == "__main__":
    data1 = date(2018, 7, 26)
    data2 = date(2019, 12, 7)
    lista = listaDatas(31, data1, data2)