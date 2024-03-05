# Programação Orientada a Objeto = Encapsulamento, Polimorfismo, Herança
# __ deixa privado apenas para a classe
'''class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


ronaldo = Pessoa('Ronaldo', 32, '123jdjdjd')
print(ronaldo.nome)
print(ronaldo.idade)
print(ronaldo.cpf)'''
# Vai printar
# Ronaldo
# 32
# 123jdjdjd
# porém se eu colocar na função self.cpf = cpf eu colocar self.__cpf = cpf deixa restrito a informação apenas para class
# mas se eu criar uma função para mostrar eu consigo ex:
'''class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def print_cpf(self):
        print(self.cpf)



ronaldo = Pessoa('Ronaldo', 32, '123jdjdjd')
ronaldo.print_cpf()'''

'''class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf   # atributo privado

    def correr(self):
        print('Estou Correndo!')

    def bebida(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()  # metodo privado
        print('Bebendo...')


    def __apresentar_documento(self): # com __ eu deixo o  metodo privado também
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', 32, '123jdjdjd')
ronaldo.bebida('cerveja')
ronaldo.bebida('coca-cola')'''
