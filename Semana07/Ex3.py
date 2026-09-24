#Crux Sacra Sit Mihi Lux

class Carro:

    def __init__(self, marca, modelo, ano):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano

def ligar():

    print("Carro ligado!")

def desligar():

    print("Carro desligado")

def main():

    carro = Carro("Porshe", "Panamera", 2010)
    ligar()
    desligar()

main()
