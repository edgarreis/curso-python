# -*- coding: UTF-8 -*-
# observer.py

''''
Observer é um padrão de design comportamental que permite definir um mecanismo 
de assinatura para notificar vários objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.
Parecido com o protocolo MQTT
'''

class Observador:

    @staticmethod
    def imprimir(nota_fiscal):
        print(f'Imprimindo nota fiscal {nota_fiscal}\n')

    @staticmethod
    def enviar_via_email(nota_fiscal):
        print(f'Enviando nota fiscal {nota_fiscal}por e-mail\n')

    @staticmethod
    def salvar_em_banco_de_dados(nota_fiscal):
        print(f'Salvando nota fiscal {nota_fiscal}no banco de dados\n')

    @staticmethod
    def atualizar_auditoria(nota_fiscal):
        print(f"Auditoria: Nova nota fiscal registrada - Razão Social: {nota_fiscal.razao_social}, CNPJ: {nota_fiscal.cnpj}")

    @staticmethod
    def atualizar_estoque(nota_fiscal):
        for item in nota_fiscal.obter_itens:
            print(f"Estoque: Atualizando estoque do item '{item.descricao}' após venda")

    @staticmethod
    def atualizar_contabilidade(nota_fiscal):
        print(f"Contabilidade: Registrando nota fiscal para fins contábeis - Valor Total: {nota_fiscal.calcular_valor_total()}")