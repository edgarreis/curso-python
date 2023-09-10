# -*- coding: UTF-8 -*-
# calculadora_de_desconto.py

''''
Chain of Responsibility é um padrão de design comportamental que permite passar
solicitações ao longo de uma cadeia de manipuladores. Ao receber uma solicitação, cada manipulador
decide processar a solicitação ou passá-la para o próximo manipulador na cadeia.
(+- um switch case de objetos)
'''


from descontos import DescontoVariosItens, DescontoAltoValor, SemDesconto

# Handler do Chain of Responsibility
class CalculadorDeDescontos:
    
    def calcula(self, orcamento):

        desconto = DescontoVariosItens(
            DescontoAltoValor(SemDesconto())
            ).calcula(orcamento)

        return desconto



if __name__ == '__main__':

    from orcamento import Orcamento, Item

    # Cria Orçamento
    orcamento = Orcamento()
    I1 = Item('Item #1', 100)
    I2 = Item('Item #2', 50)
    I3 = Item('Item #3', 400)
    orcamento.adicionar_item(I1)
    orcamento.adicionar_item(I2)
    orcamento.adicionar_item(I3)
    
    # Verifica Valor Inicial
    print("# STATUS ORÇAMENTO 1")
    print(f"     {orcamento.status}     {orcamento.desconto}")
    print("VALOR TOTAL")
    print(orcamento.valor)
    print('========================================')
    
    # Aplica Desconto
    orcamento.set_desconto_extra()

    # Verifica Valor
    print("# STATUS ORÇAMENTO 2")
    print(f"     {orcamento.status}     {orcamento.desconto}")
    print("VALOR TOTAL")
    print(orcamento.valor)
    print('========================================')
    
    # Aprova o Orçamento
    orcamento.aprova()

    # Verifica Valor
    print("# STATUS ORÇAMENTO 3")
    print(f"     {orcamento.status}     {orcamento.desconto}")
    print("VALOR TOTAL")
    print(orcamento.valor)
    print('========================================')
    
    # Aplica Desconto
    orcamento.set_desconto_extra()
    
    # Verifica Valor
    print("# STATUS ORÇAMENTO 4")
    print(f"     {orcamento.status}     {orcamento.desconto}")
    print("VALOR TOTAL")
    print(orcamento.valor)
    print('========================================')
    
    # Finaliza o Orçamento
    orcamento.finaliza()
    
    # Verifica Valor 
    print("# STATUS ORÇAMENTO 5")
    print(f"     {orcamento.status}     {orcamento.desconto}")
    print("VALOR TOTAL")
    print(orcamento.valor)
    print('========================================')

    # Verifica Desconto Extra
    calculador_de_descontos = CalculadorDeDescontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    
    print("# STATUS ORÇAMENTO - DESCONTO EXTRA")
    print(f"     {orcamento.status}     {orcamento.desconto}")
    print("VALOR TOTAL")
    print(orcamento.valor)
    print("DESCONTO CALCULADO")
    print(desconto)
    print('========================================')
    



    
