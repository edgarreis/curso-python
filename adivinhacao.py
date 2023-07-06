import random
import os
import time

def jogar():

	os.system('clear')

	print("\033[91m************************************\033[0m")
	print("\033[91m* Bem vindo ao Jogo de Adivinhação *\033[0m")
	print("\033[91m************************************\033[0m")

	time.sleep(1)
	os.system('clear')

	numero_secreto = random.randrange(1,101)
	total_de_tentativas = 0
	pontos = 1000

	print(numero_secreto)

	while(True):
		print("Qual número de dificuldade?")
		print("(1) Fácil \n(2) Médio \n(3)Dificil")
		nivel = int(input("Defina o nível: "))

		# Melhorar essa sequencia de if
		if(nivel == 1):
		        total_de_tentativas = 20
		elif(nivel == 2):
		        total_de_tentativas = 10
		else:
		        total_de_tentativas = 5

		if(nivel < 1 or nivel > 3): 
			print("Você deve digitar un número entre 1 e 3!\n")
			time.sleep(3)
			os.system('clear')
		else:
			os.system('clear')
			break

	#print("antes do for {},{}".format(nivel,total_de_tentativas))

	for rodada in range(1, total_de_tentativas + 1):

		print("Tentativa {} de {}\n".format(rodada, total_de_tentativas))
		chute = int(input("Digite o seu numero entre 1 e 100: "))
		print("Voce Digitou ", chute)

		if(chute < 1 or chute > 100):
			print("Você deve digitar un número entre 1 e 100!")
			continue 

		acertou = chute == numero_secreto
		maior   = chute >  numero_secreto
		menor   = chute <  numero_secreto

		if(acertou):
			print("Voce Acertou e fez {} pontos de 1000\n".format(pontos))
			break
		else:
			if(maior):
				print("Voce Errou! o Seu Chute Foi MAIOR do que o número secreto\n")
			elif(menor):
				print("Voce Errou! o Seu Chute Foi MENOR do que o número secreto\n")

			pontos_perdidos = abs(numero_secreto - chute)
			pontos = pontos - pontos_perdidos

		# time.sleep(3)
		# os.system('clear') 

	print("Fim de Jogo")

if(__name__ == "__main__"):
	jogar()
