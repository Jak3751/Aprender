class ControleDespesas:
    def __init__(self):
        self.__despesas = {}

    def adicionar_despesa(self, categoria, valor):
        if categoria in self.__despesas:
            self.__despesas[categoria].append(valor)
        else:
            self.__despesas[categoria] = [valor]
        print("Despesa adicionada com sucesso.")

    def visualizar_despesas(self):
        for categoria, valores in self.__despesas.items():
            total_categoria = sum(valores)
            print(f"{categoria}: {valores} (Total: {total_categoria})")

    def calcular_total_despesas(self):
        total = sum([sum(valores) for valores in self.__despesas.values()])
        print(f"Total de despesas: {total}")

