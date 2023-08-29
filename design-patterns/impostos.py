# -*- coding: UTF-8 -*-
# impostos.py

from abc import ABC, abstractmethod

''''
Decorator é um padrão de design estrutural que permite anexar novos comportamentos a objetos, 
colocando esses objetos dentro de objetos wrapper especiais que contêm os comportamentos.
'''

# Base Decorator
class DecoratorImposto(ABC):
    
    def __init__(self, outro_imposto = None):
        self._outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        
        if self._outro_imposto is None:
            return 0
        else:
            return self._outro_imposto.calcula(orcamento)
    
    @abstractmethod
    def calcula(self, orcamento):
        pass

''''
Template Method é um padrão de design comportamental que define o esqueleto de um algoritmo na superclasse, 
mas permite que as subclasses substituam etapas específicas do algoritmo sem alterar sua estrutura.
'''

# Template Parttern
class TemplateImpostoCondicional(DecoratorImposto, ABC):
    
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
        
    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass

# Decorator Python
def IPVX(metodo_calcula):
    def wrapper(self, orcamento):
        return metodo_calcula(self, orcamento) + 50.0
    return wrapper

# Strategy ISS
class ISS(DecoratorImposto):
    
    # Obrigatóriamente irá chamar o IPVX no lugar de calcula ISS, porém o próprio calcula é passado como parametro
    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)
    
# Strategy ICMS
class ICMS(DecoratorImposto):
    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)
    
class ICPP(TemplateImpostoCondicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05
    
class IKCV(TemplateImpostoCondicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.check_item_alto_valor(orcamento)
        # return orcamento.valor > 500 and any(item.valor > 100 for item in orcamento.obter_itens())

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def check_item_alto_valor(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False