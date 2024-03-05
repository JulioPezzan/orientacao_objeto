# fechado pois não tem como acrescentar sem alterar o codigo com varias funçoes...
'''class Circo:

    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Malabarista apresentando seu show')

    def apresentar_palhaco(self):
        print('Palhaço apresentando seu show')


circo = Circo()
circo.apresentar(2)
circo.apresentar(1)'''

# aberto pois posso acrescentar sem alterar o codigo
'''class Circo:

    def apresentar(self, apresentador:any):
        apresentador.apresentar_show()


class Malabarista:

    def apresentar_show(self):
        print('Malabarista apresentando seu show...')


class Palhaco:

    def apresentar_show(self):
        print('Palhaço apresentando seu show...')


class Domador:

    def apresentar_show(self):
        print('Domador apresentando seu show...')


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
domador = Domador()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
circo.apresentar(domador)'''

#RESUMO:Princípio do aberto/fechado: "O comportamento de uma classe deve estar aberta para extensão porém fechada para
# alterações." A principal idéia é que uma classe mãe deve ser genérica e abstrata para ser estendida e reaproveitada
# por classes filhas. Esse princípio rege que a classe mãe não deve ser alterada.
