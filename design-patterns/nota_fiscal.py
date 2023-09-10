# -*- coding: UTF-8 -*-
# nota_fiscal.py

from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor
        

class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observer=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens
        self.__observadores = observer

        self.registrar()

    def adicionar_observador(self, observador):
        self.__observadores.append(observador)

    def remover_observador(self, observador):
        self.__observadores.remove(observador)

    def notificar_observadores(self):
        for observer_item in self.__observadores:
            observer_item(self)
    
    def registrar(self):
        # Lógica de registro da nota fiscal
        print("Registrando nota fiscal...\n")
        self.notificar_observadores()


    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao
    
    @property
    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def detalhes(self):
        return self.__detalhes
    
    @property
    def itens(self):

        item_strings = ""   # string vazia
        for item in self.__itens:   # percorre __itens
            item_strings += f"Item: {item.descricao}, Valor: {item.valor}\n" #concatena

        return item_strings

    def __str__(self) -> str:

        item_strings = ""   # string vazia
        for item in self.__itens:   # percorre __itens
            item_strings += f"Item: {item.descricao}, Valor: {item.valor}\n" #concatena

        return (
                f"\n===================================\n"
                #f"Razão Social: {self.__razao_social}\n"
                f"CNPJ: {self.__cnpj}\n"
                #f"Data de Emissão: {self.__data_de_emissao}\n"
                #f"{item_strings}"
                #f"Detalhes: {self.__detalhes}\n"
                #f"===================================\n"
                )
    

# código das classes omitidos

if __name__ == '__main__':

    from criador_de_nota_fiscal import CriadorDeNotaFiscal
    from observer import *

    itens=[
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]
     # Builder via Python
    nota_fiscal = Nota_fiscal(
        razao_social='FHSA Limitada',
        cnpj='012345678901234',
        itens=itens,
        #data_de_emissao=date.today(),
        #detalhes=''
        observer=[Observador.imprimir,
                  Observador.enviar_via_email,
                  Observador.salvar_em_banco_de_dados,
                  Observador.atualizar_auditoria,
                  Observador.atualizar_estoque
                  ]
    )

    '''nota_fiscal_com_builder = (CriadorDeNotaFiscal()
                                .com_razao_social('FHSA Limitada')
                                .com_cnpj('012345678901234')
                                .com_itens(itens)
                                .com_data_de_emissao(date.today())
                                .builder()
                                )'''

