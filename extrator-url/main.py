
import os

os.system('clear')

# URL Base de teste
url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url0 = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url1 = " "

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia") # Gera um erro em tempo de execução

# Pesquisa por indice
# Separa base e os parametros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print("teste")
print(url_parametros)

# Pesquisa o valor de um parametro
# 1º parte
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&',indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
print("teste1")

