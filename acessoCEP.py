
import requests

class BuscaEndereco:

    def __init__(self,cep):
        cep = str(cep)
        
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido! ")
        
    def __str__(self) -> str:
        return self.formatar_cep()
    
    def validar_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def formatar_cep(self):
        # Usando ReGex
        # padrao = "([0-9]{5})([0-9]{3})"
        # cep_para_formartar = re.search(padrao, self.cep)
        # cep_formatado = f"{cep_para_formartar.group(1)}-{cep_para_formartar.group(2)}"
        # Usando Fatiamento de String
        return "{}-{}".format(self.cep[:5],self.cep[5:])

    def acessar_viacep(self):
        # monta a url no formato da API inserindo o CEP
        # url = f"https://viacep.com.br/ws/{self.cep}/json/"
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        # faz uma requisição e salva o retorno
        r = requests.get(url)
        # formata os dados no estilo json do tipo dicionário
        dados = r.json()
        # retorna 
        return (
            dados['logradouro'],
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )



