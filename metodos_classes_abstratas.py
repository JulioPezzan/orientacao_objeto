from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"


class Gato(Animal):
    def fazer_som(self):
        return "Miau!"


class Pato(Animal):
    def fazer_som(self):
        return "Quack!"


# Testando classes abstratas
# Isso vai levantar um erro, pois não podemos instanciar uma classe abstrata
# animal = Animal("Animal")

# Criando instâncias das subclasses
cachorro = Cachorro("Rex")
gato = Gato("Garfield")
pato = Pato("Donald")

# Testando os métodos das subclasses
print(cachorro.nome + " faz: " + cachorro.fazer_som())  # Saída: Rex faz: Au Au!
print(gato.nome + " faz: " + gato.fazer_som())  # Saída: Garfield faz: Miau!
print(pato.nome + " faz: " + pato.fazer_som())  # Saída: Donald faz: Quack!


#  a classe Animal é uma classe abstrata com um método abstrato fazer_som(). Essa classe não pode ser instanciada
#  diretamente porque possui um método abstrato não implementado. As subclasses Cachorro, Gato e Pato herdam da classe
#  Animal e implementam o método fazer_som() de acordo com o som característico de cada animal.
# Note que a classe Animal herda de ABC, e o método fazer_som() está decorado com @abstractmethod, indicando que este é
# um método abstrato que deve ser implementado nas subclasses. Tentar instanciar a classe Animal diretamente resultará
# em um erro.