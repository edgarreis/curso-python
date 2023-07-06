import random
import os
import time


def jogar():
	os.system('clear')

	print("\033[91m************************************\033[0m")
	print("\033[91m*    Bem vindo ao Jogo da Forca    *\033[0m")
	print("\033[91m************************************\033[0m")

	arquivo = open("palavras.txt","r")
	palavra = []

	for linha in arquivo:
		linha = linha.strip()
		palavra.append(linha)

	arquivo.close()

	# Gera um numero aleatório de 0 até o tamanho de palavra
	numero_linha = random.randrange(0,len(palavra))

	# Salva em maiusculo
	palavra_secreta = palavra[numero_linha].upper()

	# Preencha "_" para cada letra em palavra_secreta
	letras_acertadas = ["_" for letra in palavra_secreta]

	# Flags
	enforcou = False
	acertou = False
	erros = 0

	print(letras_acertadas)

	# Laço ativo enquanto o jogo não acabar
	while(not enforcou and not acertou):

		chute = input("Qual letra? ")
		chute = chute.strip().upper()

		index = 0

		if(chute in palavra_secreta):
			# Laço para varrer a palavra_secreta
			for letra in palavra_secreta:
				if(chute == letra):
					letras_acertadas[index] = letra
					#print("Encontrei a letra {} na posição {}".format(letra, index))
				index += 1
		else:
			erros += 1

		# Se erros é igual a 6 enforcou é enforcou é True e sai do laço
		enforcou = erros == 6

		# Se todos "_" forem substituidos na palavra ele sai do laço
		acertou = "_" not in letras_acertadas

		print(letras_acertadas)




	if(acertou):
		print("Parabens, você ganhou!")
	else:
		print("Você perdeu!")

	print("Fim de Jogo")

if(__name__ == "__main__"):
        jogar()
