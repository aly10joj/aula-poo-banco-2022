from src.Conta.conta import Conta


class BancoList:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta: Conta):
        self.conta.append= conta

    def procurar_conta(self, numero):
        achou = False
        for conta in self.conta:
            if conta.get_numero() == numero
                achou = True
                return conta

            if achou is False:
                return None

    def creditar(self, numero, valor):
        pass

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta inexistente!")

    def saldo(self, numero):
        pass

    def saldo(self, numero):
        pass

    def transferir(self, origem, destino, valor):
        pass