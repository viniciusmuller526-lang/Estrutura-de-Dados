#Crux Sacra Sit Mihi Lux

class Produto:

    def __init__(self, preco, quantidade):

        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):

        valor_total = self.preco * self.quantidade
        print("Valor Total: ", valor_total)

laranjinha = Produto(8, 100)
laranjinha.calcular_total()
