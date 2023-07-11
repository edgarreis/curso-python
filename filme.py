
import os

os.system('clear')

class Catalogo:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def imprimir(self):
        print(f'Nome: {self._nome} - Ano {self.ano} - Likes: {self._likes}')


class Filme(Catalogo):
    def __init__(self, nome, ano, duracao):
        # Herança da Classe mãe Catalogo para Filme
        super().__init__(nome, ano)
        self.duracao = duracao 

    def imprimir(self):
        print(f'Nome: {self._nome} - Ano {self.ano} - {self.duracao} min - Likes: {self._likes}')

    
class Serie(Catalogo):
    def __init__(self, nome, ano, temporadas):
        # Herança da Classe mãe Catalogo para Serie
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprimir(self):
        print(f'Nome: {self._nome} - Ano {self.ano} - {self.temporadas} temporadas - Likes: {self._likes}')