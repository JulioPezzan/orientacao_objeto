'''class MinhaClasse:

    estatico = 'lhama'  # variavel de classe

    def __init__(self, estado):
        self.estado = estado


obj1 =  MinhaClasse(True)
obj2 =  MinhaClasse(False)

obj1.estatico = 'Programador' # printa Programador
MinhaClasse.estatico = 'Programador'# faz printar programador em todos abaixo
obj1.estatico = 'lhama'  # printa lhama

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)'''

# @classmethod = Você deve utilizar essa marcação quando você quer criar um método de uma classe que pode ser chamado
# diretamente, sem ser instânciado.
#@classmethod= construtor
