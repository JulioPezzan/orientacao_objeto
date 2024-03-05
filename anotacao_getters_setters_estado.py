'''class Pessoa:  # quando for nomear uma CLASSE é interessante usar um SUBSTANTIVO

    # uma boa pratica também é já definir as variaveis e falar o que ela retorna
    def __init__(self, name: str, idade: int) -> None:
        self.name = name  # quando for nomear os ATRIBUTOS dessa classe também é interessante usar SUBSTANTIVO
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:  # quando for nomear os METODOS é interessante usar VERBO
        print(f'Dirigindo um(a) {veiculo}')

    def cantar(self) -> None:
        print('lalalala')

    def apresentar_idade(self) -> int:
        return self.idade'''
