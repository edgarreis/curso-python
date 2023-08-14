import re

class TelefoneBR:
    def __init__(self, telefone):
        if self.ValidarTelefoneBR(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Telefone Inválido! ")

    def __str__(self):
        return self.FormatarTelefoneBRF()

    def ValidarTelefoneBR(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,telefone)
        
        if resposta:
            return True
        else:
            return False
         
    def FormatarTelefoneBRF(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        
        resultado = re.search(padrao,self.telefone)
        ddi = resultado.group(1) if resultado.group(1) else ""
        formato = ("+" if ddi else "")+("{}({}){}-{}")

        telefone_formatado = formato.format(
            ddi,
            resultado.group(2),
            resultado.group(3),
            resultado.group(4),
        )

        return telefone_formatado