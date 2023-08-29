
# TODO ler linha e colocar proximo numero
contato = [
    '11,Carol,carol@carol.com.br\n'
    '12,Maria,m@mmaria.com.br\n'
    '13,Jose,jose@jose.com.br\n'
    '14,Calos,carlosl@carlosl.com.br\n'
]

try:
    with open('/home/echo/curso-python/arquivos/dados/contatos_escrita.csv',encoding='latin_1',mode="a+") as arquivo_contatos: # mode=a (append)

        # Escrita no arquivo
        for contato in contato:  
            arquivo_contatos.write(contato)

        # Atualiza o arquivo
        arquivo_contatos.flush()

        # Lê o arquivo
        arquivo_contatos.seek(0)
        for linha in arquivo_contatos:  
            print(linha,end='') 

except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Sem permissão de escrita")