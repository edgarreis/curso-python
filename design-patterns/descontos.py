# -*- coding: UTF-8 -*-
# desconto.py

class DescontoVariosItens():

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)


class DescontoAltoValor():

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)

class SemDesconto():

    def calcula(self, orcamento):

        return 0