class Comodo:
    __altura: float
    __largura: float
    __profundidade: float

    def __init__(self, altura, largura, profundidade):
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

    @property
    def altura(self):
        return self.__altura
    
    @property
    def largura(self):
        return self.__largura
    
    @property
    def profundidade(self):
        return self.__profundidade
    
    @altura.setter
    def altura(self, altura):
        try:
            self.__altura = float(altura)
        except Exception:
            print('O valor informado da altura é inválido!')
            exit()

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print('O valor informado da largura é inválido!')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print('O valor informado da profundidade é inválido')
            exit()



