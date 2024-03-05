class Forma:
    def calcular_area(self):
        pass


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado


def imprimir_area(forma):
    print("Área:", forma.calcular_area())


# Testando o princípio de Liskov
retangulo = Retangulo(4, 6)
quadrado = Quadrado(4)

print("Área do retângulo:")
imprimir_area(retangulo)

print("Área do quadrado:")
imprimir_area(quadrado)
# Esse codigo respeita o principio de Liskov