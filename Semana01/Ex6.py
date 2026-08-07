#Crux Sacra Sit Mihi Lux

class Aluno:

    def __init__(self, nome, lista):

        self.nome = nome
        self.lista = lista
        self.media = 0

    def calcular_media(self):

        self.media = sum(self.lista) / len(self.lista)
    
    def verificar_aprovacao(self):

        if self.media >= 7:

            print(f"Aluno {self.nome} está aprovado")
        
        else:

            print(f"Aluno {self.nome} está reprovado")

notas_clara = []
notas_rafael = []

notas_clara.extend ([8, 9, 8])
notas_rafael.extend ([0, 4, 2])

clara = Aluno("Clara", notas_clara)
rafael = Aluno("Rafael", notas_rafael)

clara.calcular_media()
clara.verificar_aprovacao()
rafael.calcular_media()
rafael.verificar_aprovacao()
