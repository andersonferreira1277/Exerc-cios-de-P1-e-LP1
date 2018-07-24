from datetime import datetime
from calendar import monthrange

def rangeMesStr(dataStr):
    """formato 07/2018"""
    """retorno duas string no formato 2018-07-01, 2018-07-31"""

    listaDeDatas = []
    dataStr = "01/"+dataStr

    data1 = datetime.strptime(dataStr, "%d/%m/%Y")
    data1Str = data1.strftime("%Y-%m-%d")

    listaDeDatas.append(data1Str)

    ultimoDiaMes = monthrange(data1.year, data1.month)
    ultimoDiaMes = ultimoDiaMes[1]
    data2Str = str(data1.year)+"-"+str(data1.month)+"-"+str(ultimoDiaMes)

    data2 = datetime.strptime(data2Str, "%Y-%m-%d")
    data2Str = data2.strftime("%Y-%m-%d")

    listaDeDatas.append(data2Str)

    return listaDeDatas

lista = rangeMesStr("02/2008")
print(lista[0])
print(lista[1])