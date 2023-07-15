
from filme import Filme, Serie, Playlist

# List
vingadores = Filme('Vingadores', 2018, 180)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico',1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
vf = Filme('Velozes e furiosos', 2010, 120)

# Likes
atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

#print(f'Nome: {vingadores.nome} - Ano {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')
#print(f'Nome: {atlanta.nome} - Ano {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

#print(f'Nome: {vingadores.nome} - Ano {vingadores.ano}')
#print(f'Nome: {atlanta.nome} - Ano {atlanta.ano}')

# List de Objetos
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #print(f'Nome: {programa.nome} - Ano {programa.ano} - D {detalhes}')
    #programa.imprimir()
    print(programa)

print("================")

#playlist_fim_de_semana.append(vf)
playlist_fim_de_semana += vf
playlist_fim_de_semana.append(vf)

for programa in playlist_fim_de_semana:
    #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #print(f'Nome: {programa.nome} - Ano {programa.ano} - D {detalhes}')
    #programa.imprimir()
    print(programa)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

filme_procurado = "Atlanta"

if filme_procurado in playlist_fim_de_semana:
    print(f'O filme {filme_procurado} está na playlist.')
else:
    print(f'O filme {filme_procurado} não está na playlist.')

"""if playlist_fim_de_semana.pesquisar(filme_procurado):
    print(f'O filme {filme_procurado} está na playlist.')
else:
    print(f'O filme {filme_procurado} não está na playlist.')"""

"""def pesquisar_nome(nome, lista):
    for filme in lista:
        if filme.nome == nome:
            return True
    return False"""

"""for programa in playlist_fim_de_semana:
    if filme_procurado == programa.nome:
        verificar = True
        break
    else:
        verificar = False"""




