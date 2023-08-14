from validate_docbr import CPF, CNPJ

class DocumentoBR:

    @staticmethod
    def create(documento):
        doc_str = str(documento)
        
        if len(doc_str) == 11:
            return Cpf(doc_str)
        if len(doc_str) == 14:
            return Cnpj(doc_str)
        else:
            raise ValueError("Documento Invalido! ")

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.ValidarCPF(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido! ")
        
    def __str__(self):
        return self.FormatarCPF()

    def ValidarCPF(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            return ValueError("Quantidade de Digitos Inválido! ")
        
    def FormatarCPF(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    

class Cnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.ValidarCNPJ(documento):
            self.cnpj = documento
        else:
            raise ValueError("cnpj inválido! ")
        
    def __str__(self):
        return self.FormatarCNPJ()

    def ValidarCNPJ(self, documento):
        if len(documento) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            return ValueError("Quantidade de Digitos Inválido! ")
        
    def FormatarCNPJ(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    

