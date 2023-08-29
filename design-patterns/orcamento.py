# -*- coding: UTF-8 -*-
# orcamento.py

from abc import ABC, abstractmethod

''''
State é um padrão de design comportamental que permite que um objeto 
altere seu comportamento quando seu estado interno muda. Parece que o objeto mudou de classe.
O padrão Estado está intimamente relacionado ao conceito de Máquina de Estados Finitos
'''

class StateOrcamento(ABC):

  @abstractmethod
  def set_desconto_extra(self, orcamento):
    pass

  @abstractmethod
  def aprova():
    pass
  
  @abstractmethod
  def reprova():
    pass

  @abstractmethod
  def finaliza():
    pass

class EmAprovacao(StateOrcamento):
  def __str__(self) -> str:
    return "Em Aprovação"
  
  def set_desconto_extra(self, orcamento):
    orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

  def aprova(self, orcamento):
    orcamento.status = Aprovado()

  def reprova(self, orcamento):
    orcamento.status = Reprovado()

  def finaliza(self, orcamento):
    raise Exception('Orçamentos Em Aprovação não podem ser Finalizados')
      
class Aprovado(StateOrcamento):
  def __str__(self) -> str:
    return "Aprovado"

  def set_desconto_extra(self, orcamento):
    orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

  def aprova(self, orcamento):
    raise Exception('Orçamentos já Aprovado')

  def reprova(self, orcamento):
    raise Exception('Orçamentos já Aprovado')

  def finaliza(self, orcamento):
    orcamento.status = Finalizado()

class Reprovado(StateOrcamento):
  def __str__(self) -> str:
    return "Reprovado"
  
  def set_desconto_extra(self, orcamento):
    raise Exception('Orçamentos reprovados não recebem desconto Extra')

  def aprova(self, orcamento):
    raise Exception('Orçamentos já Reprovado')

  def reprova(self, orcamento):
    raise Exception('Orçamentos já Reprovado')

  def finaliza(self, orcamento):
    orcamento.status = Finalizado()

class Finalizado(StateOrcamento):
  def __str__(self) -> str:
    return "Finalizado"
  
  def set_desconto_extra(self, orcamento):
    raise Exception('Orçamentos finalizados não recebem desconto Extra')

  def aprova(self, orcamento):
    raise Exception('Orçamentos já Finalizados')

  def reprova(self, orcamento):
    raise Exception('Orçamentos já Finalizados')

  def finaliza(self, orcamento):
    raise Exception('Orçamentos já Finalizados')

class Orcamento():
  
  def __init__(self):
    self.__itens = []
    self.status = EmAprovacao()
    self.__desconto_extra = 0
    self.__desconto = False  # Novo atributo para rastrear o desconto aplicado

  # Maquina de Estados
  def aprova(self):
    self.status.aprova(self)
    self.__desconto = False  # Reseta o atributo quando o status muda

  def reprova(self):
    self.status.reprova(self)
    self.__desconto = False  # Reseta o atributo quando o status muda

  def finaliza(self):
    self.status.finaliza(self)
    self.__desconto = False  # Reseta o atributo quando o status muda

  # Start
  def set_desconto_extra(self):
    self.status.set_desconto_extra(self)
    self.__desconto = True  # Atualiza o atributo quando o desconto é aplicado
  
    
  @property
  def desconto_extra(self):
      return self.__desconto_extra

  def adiciona_desconto_extra(self, novo_desconto_extra):
      self.__desconto_extra += novo_desconto_extra

  @property
  def valor(self):
    total = 0.0
    for item in self.__itens:
      total+=item.valor
    return total - self.__desconto_extra
  
  @property
  def total_itens(self):
    return len(self.__itens)
  
  @property
  def desconto(self):
    return "Desconto Aplicado" if self.__desconto else "Sem Desconto"
  
  def obter_itens(self):
    return tuple(self.__itens)
    
  def adicionar_item(self, item):
    self.__itens.append(item)

  def __str__(self) -> str:
    #return self.__valor
    return self.__itens

  
class Item():

  def __init__(self, nome, valor):
    self.__nome = nome
    self.__valor = valor

  @property
  def nome(self):
    return self.__nome
  
  @property
  def valor(self):
    return self.__valor
