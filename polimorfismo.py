class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Pato(Animal):
    def falar(self):
        return "Quack!"

def fazer_barulho(animal):
    print(animal.falar())

# Testando o polimorfismo
cachorro = Cachorro()
gato = Gato()
pato = Pato()

fazer_barulho(cachorro)  # Saída: Au Au!
fazer_barulho(gato)      # Saída: Miau!
fazer_barulho(pato)      # Saída: Quack!

# temos uma classe base Animal com um método falar(). Em seguida, temos três subclasses: Cachorro, Gato e Pato, cada uma
# delas redefine o método falar().
# A função fazer_barulho() recebe um objeto do tipo Animal como argumento e chama o método falar() sobre ele. Como cada
# uma das subclasses implementa o método falar() de maneira diferente, quando chamamos fazer_barulho() com diferentes
# instâncias das subclasses, elas produzem saídas diferentes, demonstrando o polimorfismo.