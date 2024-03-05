class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = 'Rua do Balão'
        self.sobrenome = 'Silva'


    def comer(self) -> None:
        print('Estou comendo...')


    def estudar(self) -> None:
        print('Estou estudando...')


class Filha(Mae):     # dessa forma vou conseguir usasr alguns elemnetos da classe Mãe

    def __init__(self):
        super().__init__('Rua do bolo') # super ele está se referindo ao __init__ da classe Mae


clara = Filha()
clara.estudar()

print(clara.endereco)
