
from filme import Filme, Serie

vingadores = Filme('Vingadores', 2018, 180)
atlanta = Serie('atlanta', 2018, 2)

atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()

#print(f'Nome: {vingadores.nome} - Ano {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')
#print(f'Nome: {atlanta.nome} - Ano {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

#print(f'Nome: {vingadores.nome} - Ano {vingadores.ano}')
#print(f'Nome: {atlanta.nome} - Ano {atlanta.ano}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #print(f'Nome: {programa.nome} - Ano {programa.ano} - D {detalhes}')
    programa.imprimir()