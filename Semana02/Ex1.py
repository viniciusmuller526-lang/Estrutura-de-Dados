#Crux Sacra Sit Mihi Lux

class Produto:

    def __init__(self, nome, preco, quantidade):
        
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_produto(self):

         print(f"Nome do produto: {self.nome}, Preço: {self.preco}, Quantidade em estoque: {self.quantidade}")

    def atualizar_estoque(self, quantidade_a_somar):
    
            self.quantidade += quantidade_a_somar

    def realizar_venda(self, quantidade_a_vender):

        if quantidade_a_vender > self.quantidade:

            print("Estoque insuficiente, tente de novo mais tarde")

        else:

            self.quantidade -= quantidade_a_vender

    def calcular_total(self):
    
            valor_total = self.preco * self.quantidade
            print("Valor Total: ", valor_total)

laranjinha = Produto("Laranjinha", 8, 10)
pepsi = Produto("Pepsi", 9, 20)
coca = Produto("Coca Cola", 10, 30)

coca.realizar_venda(5)
coca.mostrar_produto()
coca.atualizar_estoque(15)
coca.mostrar_produto()

laranjinha.realizar_venda(11)
laranjinha.calcular_total()
