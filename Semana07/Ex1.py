#Crux Sacra Sit Mihi Lux

class Pessoa:

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

def apresentar(pessoa):

    print(f"Nome da pessoa: {pessoa.nome}, Idade da pessoa: {pessoa.idade}")

def main():

    vinicius = Pessoa("Vinícius", 19)
    apresentar(vinicius)
    talisson = Pessoa("Tálisson", 18)
    apresentar(talisson)

main()
