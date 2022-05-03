from conta import Conta


class BancoList:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta: Conta):
        self.conta.append= conta

    def procurar_conta(self, numero: object) -> object:
        achou = False
        for conta in self.conta:
            if conta.get_numero() == numero:
                achou = True
                return conta

            if achou is False:
                return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta inexistente!")

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta inexistente!")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            conta.get_saldo()
        else:
            print ("Conta inexistente!")
     

    def transferir(self, origem, destino, valor):
        conta = self.procurar_conta(valor)
        if conta:
            