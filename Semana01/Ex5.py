#Crux Sacra Sit Mihi Lux

class Funcionario:

    def __init__(self, nome, salario, cargo):
        
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):

        if self.cargo == "Gerente":

            self.salario *= 1.1
        
        else:

            self.salario *= 1.05
        
        print(f"Salário de {self.nome}: {self.salario}")

clarisse = Funcionario("Clarisse", 2500, "Gerente")
diego = Funcionario("Diego", 1600, "Peão")

clarisse.calcular_bonus()
diego.calcular_bonus()
