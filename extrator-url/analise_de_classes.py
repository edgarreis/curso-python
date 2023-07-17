class Teste(object):
  def metodoNormal(self):
   print("Olá sou um método normal\n")
  
  @classmethod
  def metodoClass(cls, self):
    print("Sou um método de:")
    print(cls)
    print("Chamado por: ")
    print(self)
    print("\n")

  @staticmethod
  def metodoStatic():
    print("E sou um método estático")
    print("\n")


obj = Teste()

# chamando o método normal
obj.metodoNormal()

# chamando método de classe pela Class e pelo Object
Teste.metodoClass(Teste)
obj.metodoClass(obj)

# chamando método estático
obj.metodoStatic()