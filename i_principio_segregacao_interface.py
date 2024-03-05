from abc import ABC, abstractmethod

# Interface segregada em interfaces menores e mais específicas

class Aves(ABC):
    @abstractmethod
    def voar(self):
        pass

class AvesQueNadam(ABC):
    @abstractmethod
    def nadar(self):
        pass

# Implementações específicas

class Pato(Aves, AvesQueNadam):
    def voar(self):
        print("Pato voando")

    def nadar(self):
        print("Pato nadando")

class Avestruz(Aves):
    def voar(self):
        print("Avestruz não voa")

# Cliente

def testar_habilidades_aves(ave):
    if isinstance(ave, Aves):
        ave.voar()
    if isinstance(ave, AvesQueNadam):
        ave.nadar()

# Testando

pato = Pato()
avestruz = Avestruz()

print("Habilidades do pato:")
testar_habilidades_aves(pato)

print("\nHabilidades da avestruz:")
testar_habilidades_aves(avestruz)


# temos duas interfaces segregadas: Aves e AvesQueNadam. O Pato implementa ambas, pois é uma ave que pode voar e nadar.
# Por outro lado, a Avestruz implementa apenas a interface Aves, pois é uma ave que não pode nadar. Isso exemplifica o
# princípio da segregação de interface, pois cada classe implementa apenas as interfaces que são relevantes para ela.
#A função testar_habilidades_aves() é o cliente que pode interagir com diferentes tipos de aves. Ele não precisa saber
# todas as habilidades possíveis de uma ave. Em vez disso, ele simplesmente invoca métodos com base nas interfaces
# relevantes que a ave implementa. Isso ajuda a manter o código desacoplado e aderente ao princípio da segregação de
# interface.
