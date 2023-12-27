class ControleDespesas:
    def __init__(self):
        self.despesas = {}

    def adicionar_despesa(self, categoria, valor):
        if categoria in self.despesas:
            self.despesas[categoria].append(valor)
        else:
            self.despesas[categoria] = [valor]
        print("Despesa adicionada com sucesso.")

    def visualizar_despesas(self):
        for categoria, valores in self.despesas.items():
            total_categoria = sum(valores)
            print(f"{categoria}: {valores} (Total: {total_categoria})")

    def calcular_total_despesas(self):
        total = sum([sum(valores) for valores in self.despesas.values()])
        print(f"Total de despesas: {total}")

