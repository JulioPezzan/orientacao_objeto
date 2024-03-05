class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = None  # Referência para a classe Motor (agregação)

    def adicionar_motor(self, motor):
        self.motor = motor

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

# Criando instâncias das classes
motor_carro = Motor("V8")  # Instância de Motor
carro = Carro("Toyota", "Corolla")  # Instância de Carro

# Agregando o motor ao carro
carro.adicionar_motor(motor_carro)

# Acessando os atributos do carro e do motor
print("Marca do carro:", carro.marca)
print("Modelo do carro:", carro.modelo)
print("Tipo do motor do carro:", carro.motor.tipo)

#A agregação de classes é um conceito da programação orientada a objetos em que uma classe contém referências para
# outras classes, mas a relação não é tão forte quanto na composição. Na agregação, as classes associadas podem existir
# independentemente da classe principal.

#  temos duas classes: Carro e Motor. A classe Carro tem uma relação de agregação com a classe Motor, pois contém uma
#  referência para ela (self.motor). No entanto, o motor pode existir independentemente do carro.
# Ao criar uma instância de Motor e uma instância de Carro, podemos agregar o motor ao carro chamando o método
# adicionar_motor(). Em seguida, podemos acessar os atributos tanto do carro quanto do motor através da instância do
# carro. Isso ilustra a relação de agregação entre as classes.