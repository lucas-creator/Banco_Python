from conta import Conta
from conta_corrente import ContaCorrente

conta1 = ContaCorrente("Pedro Silva", "0020", "13", 5000)
conta1.deposita(2000)
conta1.saca(900)
print("Saldo da Conta:")
print(conta1.saldo)

conta2 = ContaCorrente("Paula Silva", "0020", "20", 4000)
conta1.transfere_para(conta2, 500)

print("Saldo depois da transferência:")
print(conta1.saldo)
print(conta2.saldo)
