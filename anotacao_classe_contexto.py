# aula 1 :
# classe ela possui caracteristicas(atributo); açoes(metodos) metodo é o que retorna também
# ex: classe = pessoa  caracteristicas (comer); açoes(corre)
'''class MinhaClasse:

    def meu_metodo(self):    # self é referencia na classe que ele está identado
        print('Estou no metodo') # fiz um metodo para minha classe


object = MinhaClasse()  # estancia um objeto
object.meu_metodo()     # acionando um metodo de desejo'''

'''class MinhaClasse:

    def __init__(self, att):
        self.meu_atributo = 'Olá Mundo!'
        self.meu_atributo2 = att


    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo2)


    def meu_metodo2(self, num, mult):# self é referencia na classe que ele está identado,fiz um metodo para minha classe
        return num * mult

objeto = MinhaClasse(23)    # objeto estanciado
objeto.meu_metodo()'''
# printa na tela : Olá Mundo!
# 23
