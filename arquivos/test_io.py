
arquivo = open('/home/echo/curso-python/arquivos/dados/contatos_escrita.csv',encoding='latin_1',mode="a+")

print(arquivo.buffer)

contato = bytes('15,Veronica,veronica@veronica.com.br\n',encoding='latin_1')

arquivo.buffer.write(contato)

# Lê o arquivo
arquivo.buffer.seek(0)
for linha in arquivo.buffer:  
    print(linha,end='')

arquivo.close()

