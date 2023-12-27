from lancamentos import ControleDespesas
def menu():
    print("==== Controle de Despesas ====")
    print("1. Adicionar Despesa")
    print("2. Visualizar Despesas")
    print("3. Calcular Total de Despesas")
    print("4. Sair")


if __name__ == "__main__":
    controle_despesas = ControleDespesas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            categoria = input("Digite a categoria da despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            controle_despesas.adicionar_despesa(categoria, valor)
        elif opcao == "2":
            controle_despesas.visualizar_despesas()
        elif opcao == "3":
            controle_despesas.calcular_total_despesas()
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")