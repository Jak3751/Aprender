class Produto:
#   pass  ->> utilizo se a classe fosse vazia
    def __init__(self, nome, preco = 1.99, desc = 0):
        self.nome = nome #para definir que esse atributo seja privado, consequentemente nao conseguir acessar, basta colocar assim ->> sel.__nome = nome
        self.preco = preco
        self.desc = desc

#   @property   ->> se usar, estarei definindo preco_final como variavel e não como metodo
    def preco_final(self):
        return (1 - self.desc) * self.preco

p1 = Produto('Caneta', 5.99, 0.1)
p2 = Produto('Caderno', 12.99, 0.2)

print(p1.nome, p1.preco, p1.desc, p1.preco_final())  #se usar o @property nao preciso usar o () no preco_final   #deixando atributo privado, print(p1.__nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final())  #se usar o @property nao preciso usar o () no preco_final
