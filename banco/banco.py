

from conta import Conta
from cliente import Cliente

conta1 = Conta(titular="Edgar dos Reis", saldo=500.00, limite=2000.00, numero=4011)

conta2 = Conta(3220,"Maria Santos", 100.0, 1000.00)

conta1.extrato()

conta2.extrato()

conta1.transferir(50,conta2)

conta1.extrato()

conta2.extrato()

conta1.limite

conta1.limite = 5000.00

conta1.extrato()

titular1 = conta1.titular

saldo1 = conta1.saldo

print("Titular 1 {}, Saldo 1 {}".format(titular1, saldo1))

conta1.sacar(10000.00)

conta1.extrato()

conta1.sacar(5000.00)

conta1.extrato()
