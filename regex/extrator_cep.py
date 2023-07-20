import re   #RegEx

Endereco = "Rua São Januário, 13, Monte Santo, Almirante Tamandaré, 83501480"

# 5 digitos + hífen (opcional) + 3 digitos 

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(Endereco) # Match

if busca:
    cep = busca.group()
    print(cep)