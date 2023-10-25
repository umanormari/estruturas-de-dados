class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.get_nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()

print(conta.titular, "Conta-Corrente:", conta.numero, "Seu saldo: R$ ", conta.saldo)

"""3 ASPAS: O texto é escrito entre aspas simples ou duplas e permite a inserção de múltiplas linhas."""