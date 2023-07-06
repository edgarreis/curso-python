import random
import os
import time

import forca
import adivinhacao


def escolher_jogo():

	os.system('clear')

	print("\033[91m************************************\033[0m")
	print("\033[91m*         Escolha seu Jogo         *\033[0m")
	print("\033[91m************************************\n\n\033[0m")



	while(True):
		print("(1) Jogo da Forca \n(2) Jogo da Adivinhação\n")
		jogo = int(input("Qual jogo: "))

	        # Melhorar essa sequencia de if
		if(jogo == 1):
			print("Abrindo Forca\n")
			forca.jogar()
		elif(jogo == 2):
			print("Abrindo AdivinhaçãoForca\n")
			adivinhacao.jogar()
		if(jogo < 1 or jogo > 2):
			print("Você deve digitar un número entre 1 e 2!\n")
			time.sleep(2)
			os.system('clear')
		else:
			#os.system('clear')
			break

	print("Fechando jogos")

if(__name__ == "__main__"):
	escolher_jogo()
