from documentosBR import *
from telefonesBR import *
from datasBR import *
from acessoCEP import *

# Trabalhando com Documentos BR
#doc = input("Digite o Documento: ")
doc = "392.475.380-68"
ob_doc = DocumentoBR.create(doc)
print(ob_doc)

# 19.827.222/0001-00
# 392.475.380-68

# Trabalhando com Telefones
telefone = "553419888776655"
fone = TelefoneBR(telefone)
print(fone)

# Trabalhando com Datas
cadastro = DatasBR()
print(cadastro.tempo_cadastro())

# Trabalhando com Endereços
cep = 83500400
obj_cep = BuscaEndereco(cep)
logradouro, bairro, cidade, uf = obj_cep.acessar_viacep()
b = obj_cep.acessar_viacep()
print(logradouro, bairro, cidade, uf)

