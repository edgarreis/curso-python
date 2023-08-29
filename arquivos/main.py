import contatos_utils

caminho_csv = '/home/echo/curso-python/arquivos/dados/contatos.csv'
caminho_pickle = '/home/echo/curso-python/arquivos/dados/contatos.p'
caminho_json = '/home/echo/curso-python/arquivos/dados/contatos.json'
encoding = 'latin_1'

def main():
    while True:
        print("Menu:")
        print("1. Ler contatos do CSV")
        print("2. Gravar contatos em formato Pickle")
        print("3. Ler contatos em formato Pickle")
        print("4. Gravar contatos em formato JSON")
        print("5. Ler contatos em formato JSON")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            # Ler contatos do CSV
            contatos_origem = contatos_utils.ContatoDAO.csv_contatos(caminho_csv, encoding)
            print_contatos(contatos_origem, "Contatos lidos do CSV:")

        elif escolha == '2':
            # Gravar contatos em formato Pickle
            contatos = contatos_utils.ContatoDAOpickle.save(contatos_origem, caminho_pickle)
            print("Contatos gravados em formato Pickle.")
        elif escolha == '3':
            # Ler contatos em formato Pickle
            contatos = contatos_utils.ContatoDAOpickle.seek(caminho_pickle)
            print_contatos(contatos, "Contatos lidos em formato Pickle:")
        elif escolha == '4':
            # Gravar contatos em formato JSON
            contatos_utils.ContatoDAOJSON.save(contatos_origem, caminho_json)
            print("Contatos gravados em formato JSON.")
        elif escolha == '5':
            # Ler contatos em formato JSON
            contatos = contatos_utils.ContatoDAOJSON.seek(caminho_json)
            print_contatos(contatos, "Contatos lidos em formato JSON:")
        elif escolha == '6':
            # Sair
            print("Saindo...")
            break
        else:
            # Opção inválida
            print("Opção inválida. Escolha novamente.")

def print_contatos(contatos, mensagem):
    print(mensagem)
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

if __name__ == "__main__":
    main()
