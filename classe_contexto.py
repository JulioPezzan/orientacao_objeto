class ControleRemoto:

    def __init__(self, televisao, comodo):   # metodo construtor com atributos televisao e comodo
        self.televisao = televisao
        self.comodo = comodo
        # agora televisao e comodo são dois atributos que estão no mesmo contexto da minha classe

    def avancar_canal(self):
        print('Canal Avancado')

    def voltar_canal(self):
        print('Voltar o Canal')

    def escolher_canal(self, canal):
        print(f'Alterando para o canal: {canal}')


controle_sala = ControleRemoto('Sansung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

controle_quarto = ControleRemoto('LG', 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)
