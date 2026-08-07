#Crux Sacra Sit Mihi Lux

class Livro:

    def __init__(self, titulo, autor, num_pag):
        
        self.titulo = titulo
        self.autor = autor
        self.num_pag = num_pag

    def tamanho_livro(self):

        if self.num_pag > 100:

            print(f"Livro {self.titulo} é longo")
        
        else:

            print(f"Livro {self.titulo} é curto")

lotr = Livro("Senhor dos Anéis", "J.R.R. Tolkiem", 300)
rev_dos_bichos = Livro("A Revolução dos Bichos", "George Orwell", 90)

lotr.tamanho_livro()
rev_dos_bichos.tamanho_livro()
