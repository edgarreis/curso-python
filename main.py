from documentosBR import *
from telefonesBR import *
from datasBR import *
from acessoCEP import *
import re

''''
doc = input("Digite o Documento: ")

ob_doc = Documento.create(doc)

print(ob_doc)


# 19.827.222/0001-00
# 392.475.380-68
telefone = "55341987031286"

fone = TelefoneBR(telefone)

print(fone)


cadastro = DatasBR()

print(cadastro.tempo_cadastro())
'''''
cep = 83501480

obj_cep = BuscaEndereco(cep)

logradouro, bairro, cidade, uf = obj_cep.acessar_viacep()

b = obj_cep.acessar_viacep()

print(logradouro, bairro, cidade, uf)