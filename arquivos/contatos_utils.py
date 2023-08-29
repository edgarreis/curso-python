from abc import ABC, abstractmethod
import csv
import pickle
import json
from contato import Contato

class ContatoDAO(ABC):

    @abstractmethod
    def seek(self, path):
        pass

    @abstractmethod
    def save(self, contacts, path):
        pass

    # cria uma lista para importar os dados do csv
    def csv_contatos(caminho: str, encoding: str='latin_1') -> list:
        contatos = []
        
        with open(caminho,encoding=encoding) as arquivo:
            # método de leitura do csv
            leitor = csv.reader(arquivo)
            
            # List Comprehension
            contatos = [Contato(id, nome, email) for id, nome, email in leitor]

            '''
            for linha in leitor:
                # percorre o csv
                id = linha[0]
                nome = linha[1]
                email = linha[2]

                # cria um obj e passa os atributos
                contato = Contato(id,nome,email)
                contatos.append(contato)
            '''
        return contatos


class ContatoDAOpickle(ContatoDAO):

    # Converte e salva a lista para pickes(obj serializado)
    @abstractmethod
    def save(contatos: Contato, caminho: str):
        with open(caminho, mode='wb') as arquivo:
            pickle.dump(contatos, arquivo)

    # Converte pickes para lista
    @abstractmethod
    def seek(caminho:str, encoding: str='latin_1') -> list:
        with open(caminho, mode='rb') as arquivo:
            contatos = pickle.load(arquivo,encoding=encoding)

        return contatos


class ContatoDAOJSON(ContatoDAO):

    # Converte e salva a lista para JSON
    @abstractmethod
    def save(contatos: Contato, caminho: str):
        with open(caminho, mode='w') as arquivo:
            # código omitido - Função Lambda - Função anônima (lambada input: output)
            json.dump(contatos, arquivo, default=lambda contato: contato.__dict__)
            
            #json.dump(contatos, arquivo, default=_contatos_json)
    
    # Sugestão anterior ao lambda
    def _contatos_json(contato):
        return contato.__dict__

    # Converte json para lista
    @abstractmethod
    def seek(caminho:str) -> list:
        contatos = []

        with open(caminho) as arquivo:
            contatos_json = json.load(arquivo)

            # List Comprehension
            contatos = [Contato(**contato) for contato in contatos_json]
            
            '''
            for contato in contatos_json:
                c = Contato(**contato)
                contatos.append(c)
            '''
        return contatos