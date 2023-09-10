# auditoria_observer.py
class AuditoriaObserver:
    def atualizar(self, nota_fiscal):
        print(f"Auditoria: Nova nota fiscal registrada - Razão Social: {nota_fiscal.razao_social}, CNPJ: {nota_fiscal.cnpj}")

# estoque_observer.py
class EstoqueObserver:
    def atualizar(self, nota_fiscal):
        for item in nota_fiscal.itens:
            print(f"Estoque: Atualizando estoque do item '{item.descricao}' após venda")

# contabilidade_observer.py
class ContabilidadeObserver:
    def atualizar(self, nota_fiscal):
        print(f"Contabilidade: Registrando nota fiscal para fins contábeis - Valor Total: {nota_fiscal.calcular_valor_total()}")

# nota_fiscal.py
class NotaFiscal:
    def __init__(self, razao_social, cnpj, itens):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__observadores = []

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def itens(self):
        return self.__itens

    def adicionar_observador(self, observador):
        self.__observadores.append(observador)

    def remover_observador(self, observador):
        self.__observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self.__observadores:
            observador.atualizar(self)

    def registrar(self):
        # Lógica de registro da nota fiscal
        print("Registrando nota fiscal...")
        self.notificar_observadores()

# criador_de_nota_fiscal.py
class CriadorDeNotaFiscal:
    # ... (implementação do CriadorDeNotaFiscal)
    pass

# main.py
if __name__ == '__main__':

    from nota_fiscal import Nota_fiscal
    from auditoria_observer import AuditoriaObserver
    from observer import Observador
    #from contabilidade_observer import ContabilidadeObserver

    itens = [
        # ... (lista de itens da nota fiscal)
    ]

    nota_fiscal = NotaFiscal('Empresa X', '123456789', itens)

    auditoria_observer = AuditoriaObserver()
    estoque_observer = EstoqueObserver()
    contabilidade_observer = ContabilidadeObserver()

    nota_fiscal.adicionar_observador(auditoria_observer)
    nota_fiscal.adicionar_observador(estoque_observer)
    nota_fiscal.adicionar_observador(contabilidade_observer)

    nota_fiscal.registrar()
