import random
import os
import time


def jogar():
	os.system('clear')

	print("\033[91m************************************\033[0m")
	print("\033[91m*    Bem vindo ao Jogo da Forca    *\033[0m")
	print("\033[91m************************************\033[0m")

	palavra_secreta = "teste"
	letras_acertadas = ["_","_","_","_","_"]
	enforcou = False
	acertou = False

	print(letras_acertadas)

	# Laço ativo enquanto o jogo não acabar
	while(not enforcou and not acertou):

		chute = input("Qual letra? ")
		chute = chute.strip()

		index = 0

		# Laço para varrer a palavra_secreta
		for letra in palavra_secreta:
			if(chute.upper() == letra.upper()):
				letras_acertadas[index] = letra
				#print("Encontrei a letra {} na posição {}".format(letra, index))
			index += 1



		print(letras_acertadas)
















	print("Fim de Jogo")

if(__name__ == "__main__"):
        jogar()
