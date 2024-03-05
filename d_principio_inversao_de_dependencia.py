from abc import ABC, abstractmethod

class Leitor(ABC):
    @abstractmethod
    def ler(self):
        pass

class LeitorArquivo(Leitor):
    def ler(self):
        return "Conteúdo do arquivo lido"

class Processador:
    def __init__(self, leitor):
        self.leitor = leitor

    def processar(self):
        conteudo = self.leitor.ler()
        # Processamento do conteúdo
        return "Conteúdo processado: " + conteudo

# Utilizando as classes

leitor = LeitorArquivo()
processador = Processador(leitor)
print(processador.processar())

#  a classe Processador depende de uma abstração Leitor, e não de uma implementação concreta como LeitorArquivo. Isso
#  segue o princípio da inversão da dependência, pois a classe de alto nível (Processador) depende de uma abstração
#  (Leitor), e não de uma classe de baixo nível (LeitorArquivo). Isso torna o código mais flexível e extensível,
#  já que podemos introduzir novas implementações de Leitor sem alterar o código de Processador
