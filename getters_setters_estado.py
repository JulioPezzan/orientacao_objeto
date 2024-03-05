class Alarme:

    def __init__(self, estado:bool) -> None:
        self.__estado = estado
        self.idade = idade

    def get_estado(self)-> bool:
            return self.__estado

    def set_estado(self, valor:bool) -> None:
        if isinstance(valor, bool):  # verificar o que retorna
            self.__estado = valor

''' get e set permitir que atributos privados da classe possam ser buscados/modificados fora dela - sendo que devem ser
 criados conforme necessidade. A sintaxe básica é set_nome-do-atributo e get_nome-do-atributo'''
