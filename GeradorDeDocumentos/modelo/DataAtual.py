#!/urb/bin/env python
# _*_ coding: utf-8 _*_

import time


class DataAtual:

    @staticmethod
    def getData():
        """Retorna uma string com a data no formato dia/mes/ano"""
        data = time.strftime('%d/%m/%Y')
        return data

    @staticmethod
    def getDataPorExtenso():
        """Retorno uma string com a data atual por extenso em português. ex. dezone dias do mês
        dezembro de dois mil e dezessete"""

        complementoAos = 'aos'
        complementoDia = 'dias'

        meses = {1:'janeiro', 2:'fevereiro', 3:'março', 4:'abril', 5:'maio', 6:'junho', 7:'julho',
                 8:'agosto',9:'setembro', 10:'outubro', 11:'novembro', 12:'dezembro'}

        unidades = {0:"", 1:"um", 2:"dois", 3:"três", 4:"quatro",
                    5:"cinco", 6:"seis", 7:"sete", 8:"oito", 9:"nove"}

        dezenas = {10:"dez", 11:"onze", 12:"doze", 13:"treze", 14:"quatorze", 15:"quinze",
                   16:"dezesseis", 17:"dezessete", 18:"dezoito", 19:"dezenove",
                   20:"vinte", 30:"trinta"}

        numerais = {0:"", 1:"primeiro", 2:"segundo", 3:"terceiro", 4:"quarto",
                    5:"quinto", 6:"sexto", 7:"setimo", 8:"oitavo", 9:"nono"}

        dia, mes, ano = str(time.strftime('%d/%m/%Y')).split('/')
        dia, mes, ano = map(int, [dia, mes, ano])
        diaPorExtenso = str()
        if dia:
            if dia < 10:
                diaPorExtenso = numerais[dia]
                complementoAos = 'ao'
                complementoDia = 'dia'
            elif dia >= 10 and dia < 21:
                diaPorExtenso = dezenas[dia]
            elif dia >= 21 and dia < 30:
                diaPorExtenso = dezenas[20]+' e '+ unidades[dia%20]
            elif dia == 30:
                diaPorExtenso = dezenas[dia]
            elif dia >=31 and dia < 40:
                diaPorExtenso = dezenas[30]+' e '+ unidades[dia%30]

        mesPorExtenso = meses[mes]

        anoPorExtenso = 'dois mil e '

        if ano:
            if ano%2000 < 21:
                anoPorExtenso = anoPorExtenso+dezenas[ano%2000]
            elif ano%2000 >= 21:
                anoPorExtenso = anoPorExtenso+dezenas[ano%2000]+' e '+unidades[(ano%2000)%20]
            elif ano%2000 == 30:
                anoPorExtenso = anoPorExtenso + dezenas[ano % 2000]
            elif ano%2000 >= 31:
                anoPorExtenso = anoPorExtenso+dezenas[ano%2000]+' e '+unidades[(ano%2000)%30]

        dataPorExtenso = '{} {} {} do mês de {} de {}'.format(complementoAos, diaPorExtenso, complementoDia,  mesPorExtenso, anoPorExtenso)
        return dataPorExtenso
