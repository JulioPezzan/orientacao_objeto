from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def metodo1(self):
        pass

    @abstractmethod
    def metodo2(self):
        pass


class Implementacao1(Interface):
    def metodo1(self):
        print("Implementação 1 - Método 1")

    def metodo2(self):
        print("Implementação 1 - Método 2")


class Implementacao2(Interface):
    def metodo1(self):
        print("Implementação 2 - Método 1")

    def metodo2(self):
        print("Implementação 2 - Método 2")


# Testando as implementações
impl1 = Implementacao1()
impl2 = Implementacao2()

impl1.metodo1()  # Saída: Implementação 1 - Método 1
impl1.metodo2()  # Saída: Implementação 1 - Método 2

impl2.metodo1()  # Saída: Implementação 2 - Método 1
impl2.metodo2()  # Saída: Implementação 2 - Método 2

# Embora Python não tenha uma implementação nativa de interfaces como algumas outras linguagens orientadas a objetos
# (por exemplo, Java), é possível usar convenções e recursos da linguagem para simular comportamentos semelhantes

#Embora Python não exija que você implemente explicitamente uma interface, seguir esse padrão pode ser útil para
# garantir que as classes tenham métodos específicos em comum, mesmo que não haja uma herança direta entre elas. Isso
# ajuda a garantir um contrato mínimo de funcionalidade, semelhante ao conceito de interface em outras linguagens de
# programação.