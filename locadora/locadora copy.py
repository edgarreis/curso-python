
from locadora.filme import *

def main():
    catalogo = []  # Lista para armazenar os filmes e séries

    # Adicionando alguns filmes e séries ao catálogo
    filme1 = Filme('O Senhor dos Anéis: A Sociedade do Anel', 2001, 178)
    filme2 = Filme('O Senhor dos Anéis: As Duas Torres', 2002, 179)
    filme3 = Filme('O Senhor dos Anéis: O Retorno do Rei', 2003, 201)
    serie1 = Serie('Game of Thrones', 2011, 8)
    serie2 = Serie('Breaking Bad', 2008, 5)

    catalogo.append(filme1)
    catalogo.append(filme2)
    catalogo.append(filme3)
    catalogo.append(serie1)
    catalogo.append(serie2)

    # Criando uma playlist e adicionando alguns itens
    minha_playlist = Playlist('Favoritos', [filme1, filme2, serie1])

    # Exibindo informações do catálogo
    print('--- Catálogo ---')
    for item in catalogo:
        print(item)

    print('')

    # Exibindo informações da playlist
    print('--- Minha Playlist ---')
    for item in minha_playlist.listagem:
        print(item)

    print('')

    # Dar like em um filme
    filme1.dar_like()

    # Alterar o nome de uma série
    serie1.nome = 'A Guerra dos Tronos'

    # Exibindo informações atualizadas do catálogo
    print('--- Catálogo Atualizado ---')
    for item in catalogo:
        print(item)

    print('')

    # Exibindo informações atualizadas da playlist
    print('--- Minha Playlist Atualizada ---')
    for item in minha_playlist.listagem:
        print(item)

    print('')

if __name__ == '__main__':
    main()