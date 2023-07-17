
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
    

extrator_url = ExtratoURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
valor_quantidade = extrator_url.get_valor_parametro("moedaOrigem")
print(valor_quantidade)