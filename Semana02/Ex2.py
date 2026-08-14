#Crux Sacra Sit Mihi Lux

class ContaBancaria:

    def __init__(self, nome_titular, numero_conta, saldo):
            
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def mostrar_conta(self):
    
        print(f"Saldo da conta de {self.nome_titular}: {self.saldo} reais")

    def realizar_deposito(self, quantidade_a_depositar):

        if quantidade_a_depositar > 0:

            self.saldo += quantidade_a_depositar

        else:

            print("Valor inválido")

    def realizar_saque(self, quantidade_a_sacar):
    
            if quantidade_a_sacar <= self.saldo:

                if quantidade_a_sacar > 0:
    
                    self.saldo -= quantidade_a_sacar

                else:

                    print("Valor inválido")
    
            else:

                print("Saldo insuficiente")

    def trasferir_valor(self, contas_banco, conta_destino, quantidade_a_trasferir):

    
        if quantidade_a_trasferir > self.saldo:
    
            print("Saldo insuficiente")
    
        else:

            if quantidade_a_trasferir > 0:

                for contas in contas_banco:
                    
                    if conta_destino == contas.numero_conta:

                        contas.saldo += quantidade_a_trasferir
                        self.saldo -= quantidade_a_trasferir
                        return

                print("Conta n encontrada")

            else:

                print("Valor inválido")

conta_vinicius = ContaBancaria("Vinícius", 1414, 3000)
conta_pedro = ContaBancaria("Pedro", 1313, 1000)
contas_banco = [conta_vinicius, conta_pedro]

conta_vinicius.mostrar_conta()
conta_vinicius.realizar_saque(1000)
conta_vinicius.mostrar_conta()
conta_vinicius.realizar_deposito(500)
conta_vinicius.mostrar_conta()

conta_pedro.realizar_saque(1500)
conta_pedro.realizar_deposito(0)
conta_pedro.trasferir_valor(contas_banco, 1414, 100)
conta_pedro.mostrar_conta()
conta_vinicius.mostrar_conta()
