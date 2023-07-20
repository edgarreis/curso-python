
import os
from abc import ABCMeta, abstractmethod # Importação da classe abstrata

os.system('clear')

class Catalogo(metaclass = ABCMeta):
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

    @abstractmethod # método abstrato
    def __str__(self):
        pass

    def __eq__(self, busca):
        return self._nome == busca.nome

class Filme(Catalogo):
    def __init__(self, nome, ano, duracao):
        # Herança da Classe mãe Catalogo para Filme
        super().__init__(nome, ano)
        self.duracao = duracao 

    def __str__(self):
        return f'Nome: {self._nome} - Ano {self.ano} - {self.duracao} min - Likes: {self._likes}'

    
class Serie(Catalogo):
    def __init__(self, nome, ano, temporadas):
        # Herança da Classe mãe Catalogo para Serie
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):

        return f'Nome: {self._nome} - Ano {self.ano} - {self.temporadas} temporadas - Likes: {self._likes}'

class Playlist():
    def __init__(self, nome, catalogos):
        self.nome = nome
        self._catalogos = catalogos
    
    def __getitem__(self, item):
        return self._catalogos[item]

    """ # Trecho de codigo comentado após implementar 
    __getitem__ e __len__ com duck typing

    # Reuso da List por Composição - Playlist contêm listagem
    @property
    def listagem(self):
        return self._catalogos
    
    # Reuso da List por Composição - Playlist contêm tamanho
    @property
    def tamanho(self):
        return len(self._catalogos)
    """

    def __add__(self, item):
        #ad = [item]
        #ad = Playlist('fim de semana', item)
        return self._catalogos + [item]
    
    #def __append__(self, item):
    #   return self._catalogos.append(item)

    def __append__(self, item):
        ad = [item]
        #ad = Playlist('fim de semana', item)
        return self._catalogos.append(ad)
    
    def __len__(self):
        #ad = [item]
        #ad = Playlist('fim de semana', item)
        return len(self._catalogos)

    # OPÇAO DE PESQUISA #1
    @property
    def pesquisar(self, filme_procurado):
        for programa in self._catalogos:
            if filme_procurado == self._catalogos[programa].nome:
                return True
        return False

    # OPÇAO DE PESQUISA #2
    def __contains__(self, filme_procurado):
        for programa in self._catalogos:
            if filme_procurado == programa.nome:
                return True
        return False

