
class Conta:

	# Função Construtora
	def __init__(self, numero, titular, saldo, limite):

		print("Construindo o objeto ...{}".format(self))

		# Parametros/Atributos privados
		self.__numero = numero
		self.__titular = titular
		self.__saldo = saldo
		self.__limite = limite

	# Métodos
	def extrato(self):

		print("Saldo {} do titular {} com limite de {}".format(self.__saldo, self.__titular,self.__limite))

	def depositar(self,valor):

		self.__saldo += valor

	# Método privado
	def __pode_sacar(self, valor_a_sacar):

		valor_disponivel = self.__saldo + self.__limite
		return valor_a_sacar <= valor_disponivel

	def sacar(self,valor):

		if(self.__pode_sacar(valor)):
			self.__saldo -= valor

		else:
			print("O Valor {} passou o limite".format(valor))

	def transferir(self,valor,destino):

		# Metodos sacar e depositar
		self.sacar(valor)
		destino.depositar(valor)

	@property
	def saldo(self):

		return self.__saldo

	@property
	def titular(self):

		return self.__titular

	@property
	def limite(self):

		return self.__limite

	@limite.setter
	def limite(self,limite):

		self.__limite = limite



	# Métodos estáticos
	@staticmethod
	def codigo_banco():
		return "001"

	@staticmethod
	def codigos_bancos():
		return {'BB':'001', 'Caixa':'104', 'Bradesco':'273'}


