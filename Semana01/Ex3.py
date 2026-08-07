#Crux Sacra Sit Mihi Lux

class Produto:

    def __init__(self, nome, preco, quantidade):
        
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_estoque(self, quantidade_a_somar):

        self.quantidade += quantidade_a_somar
        
    def mostrar_quant_em_estoque(self):

        print(f"Quantidade em estoque de {self.nome}: {self.quantidade}")

laranjinha = Produto("Laranjinha", 8, 100)
laranjinha.mostrar_quant_em_estoque()
laranjinha.atualizar_estoque(50)
laranjinha.mostrar_quant_em_estoque()
