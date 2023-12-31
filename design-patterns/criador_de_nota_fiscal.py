
# -*- coding: UTF-8 -*-
# criador_de_nota_fiscal.py

from datetime import date
from nota_fiscal import Nota_fiscal

''''
Builder é um padrão de design criacional que permite construir objetos complexos passo a0 passo. 
O padrão permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção.
Usado quando se quer tirar os atributos volumosos e substituir por métodos, ter um construtor unico que sabe diferenciar as variações das classes,
diferentes representações/interfaces do mesmo produdo e por fim, pode ser criar uma sequencia de criação passo a passo, primeiramente vc estancia a classe e
conforme a necessidade, vai incorporando a caractisticas (construção passo a passo do objeto em tempo de execução)
'''

# 
class CriadorDeNotaFiscal:
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = None
        self.__itens = None


    def builder(self):
        if self.__razao_social is None:
            raise Exception('Razão Social deve ser preenchida')
        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchida')
        if self.__itens is None:
            raise Exception('Itens deve ser preenchido')
        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()
        if self.__detalhes is None:
            self.__detalhes = ''
        
        nota_fiscal = Nota_fiscal(
            razao_social = self.__razao_social,
            cnpj = self.__cnpj,
            data_de_emissao = self.__data_de_emissao,
            detalhes = self.__detalhes,
            itens = self.__itens
        )
        
        return nota_fiscal
        

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self
    
    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self
    
    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self
    
    def com_itens(self, itens):
        self.__itens = itens
        return self