import re
import os
from abc import ABCMeta, abstractmethod # Importação da classe abstrata

os.system('clear')

class ExtratoURL:
    def __init__(self, url):
        self.url = ExtratoURL.sanitiza_url(url)
        self.valida_url()

    # método estático 
    # Não necessita instância e não possui "self."
    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:    # Verificar se o tipo da url é str
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if not self.url:    # if not bool(self.url):
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é valida.")

        print("A URL é valida")

    # TODO Substitur get_s por @property    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&',indice_valor)
        
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def __len__(self):
        return len(self.url)
    
    def __eq__(self, other):
        return self.url == other.url
    
    @abstractmethod # método abstrato
    def __str__(self):
        return self.url
    

extrator_url = ExtratoURL("www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
extrator_url2 = ExtratoURL("www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")

valor_quantidade = extrator_url.get_valor_parametro("moedaDestino")
print(valor_quantidade)
print("O tamanho da URL:",len(extrator_url))
print(extrator_url)
print(extrator_url == extrator_url2)