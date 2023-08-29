import contatos_utils

caminho_csv = '/home/echo/curso-python/arquivos/dados/contatos.csv'
caminho_pickle = '/home/echo/curso-python/arquivos/dados/contatos.p'
caminho_json = '/home/echo/curso-python/arquivos/dados/contatos.json'
encoding = 'latin_1'

try:
    # atribuindo a uma lista os dados do CSV
    contatos_origem = contatos_utils.ContatoDAO.csv_contatos(caminho_csv,encoding)

    for contato in contatos_origem:
        print(f'csv_contatos - {contato.id} - {contato.nome} - {contato.email}')
    
    # Antes da class
    #contatos_utils.contatos_pickle(contatos,caminho_pickle)
    #contatos = contatos_utils.pickles_contatos(caminho_pickle)

    # Converte a List em Pickle
    #contatos_utils.ContatoDAOpickle.save(contatos_origem, caminho_pickle)
    
    # Converte Pickle em List
    contatos = contatos_utils.ContatoDAOpickle.seek(caminho_pickle)
    
    for contato in contatos:
        print(f'ContatoDAOpickle - {contato.id} - {contato.nome} - {contato.email}')

    # Antes da class
    #contatos_utils.contatos_json(contatos, caminho_json)
    #contatos = contatos_utils.json_contatos(caminho_json)
    
    # Converte a List em JSON
    #contatos_utils.ContatoDAOJSON.save(contatos, caminho_json)

    # Converte JSON em List
    contatos = contatos_utils.ContatoDAOJSON.seek(caminho_json)

    for contato in contatos:
        print(f'ContatoDAOJSON - {contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Sem permissão de escrita")

