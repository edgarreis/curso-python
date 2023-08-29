# -*- coding: UTF-8 -*-
# calculadora_de_impostos.py

import time

'''
Strategy é um padrão de design comportamental que transforma um conjunto de
comportamentos em objetos e os torna intercambiáveis dentro do objeto de contexto original.
'''

# Context of Strategy
class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print(valor)

if __name__ == '__main__':

    tempo_inicial = time.time()

    from orcamento import Orcamento, Item
    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento()

    I1 = Item('Item #1', 50)
    I2 = Item('Item #2', 200)
    I3 = Item('Item #3', 250)

    orcamento.adicionar_item(I1)
    orcamento.adicionar_item(I2)
    orcamento.adicionar_item(I3)

    calculador_de_impostos = Calculador_de_impostos()
    
    print("ISS e ICMS")
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

    print("ISS com ICMS")
    calculador_de_impostos.realiza_calculo(orcamento, ISS(ICMS()))

    print("ICPP e IKCV")
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())

    print("ICPP com IKCV")
    calculador_de_impostos.realiza_calculo(orcamento, ICPP(IKCV()))

    tempo_final = time.time()

    # Teste offtopic para verificar tempo de execução
    print("\nTempo total de execução: {tempo_total} ms".format(
        tempo_total=str((tempo_final - tempo_inicial)*1000))
    )

