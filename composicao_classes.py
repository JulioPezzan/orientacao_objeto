class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("V8")  # Instância de Motor como componente de Carro

# Criando instância de Carro
carro = Carro("Toyota", "Corolla")

# Acessando os atributos do carro e do motor
print("Marca do carro:", carro.marca)
print("Modelo do carro:", carro.modelo)
print("Tipo do motor do carro:", carro.motor.tipo)

# Na composição de classes, uma classe (classe composta) é composta por objetos de outras classes (componentes).
# A relação entre a classe composta e seus componentes é forte, o que significa que se a classe composta for destruída,
# seus componentes também serão.

# temos duas classes: Motor e Carro. Na classe Carro, há uma instância da classe Motor, que é criada quando um carro é
# instanciado. Essa relação é uma relação de composição, porque o motor é um componente essencial do carro e, se o
# carro for destruído, o motor também será.
# Ao criar uma instância de Carro, o motor é criado automaticamente e atribuído à propriedade motor da instância do
# carro. Podemos acessar os atributos do motor através da instância do carro. Isso exemplifica a relação de composição
# entre as classes.