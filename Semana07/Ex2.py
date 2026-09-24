#Crux Sacra Sit Mihi Lux

class Retangulo:

    def __init__(self, altura, largura):

        self.altura = altura
        self.largura = largura

def calcular_area(retangulo):

    print(f"A área do retângulo é de: {retangulo.altura*retangulo.largura}")

def calcular_perimetro(retangulo):

    print(f"O perímetro do retângulo é de: {retangulo.altura+retangulo.largura+retangulo.altura+retangulo.largura}")

def main():

    retangulo = Retangulo(10, 20)
    calcular_area(retangulo)
    calcular_perimetro(retangulo)

main()
