class Pessoaa:

    def se_apresentar(self):
        print('Olá! Sou a pessoa A')


class Pessoab(Pessoaa):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print('Olá! Estou alterando esse metodo')


pessoa = Pessoaa()
pessoa.se_apresentar()

pessoa2 = Pessoab()
pessoa2.se_apresentar()

# Esse codigo NÃO respeita o principio de Liskov