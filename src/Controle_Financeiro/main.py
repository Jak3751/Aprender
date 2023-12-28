from funcoes import conectar_banco, lancar_despesa, excluir_despesa, consultar_despesas, fechar_conexao

def menu():
    print("==== Sistema de Controle de Despesas ====")
    print("1. Lançar Despesa")
    print("2. Excluir Despesa")
    print("3. Consultar Despesas")
    print("4. Sair")

def main():
    conexao = conectar_banco()

    if conexao:
        while True:
            menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                lancar_despesa(conexao)
            elif opcao == "2":
                id_despesa = int(input("Digite o ID da despesa a ser excluída: "))
                excluir_despesa(conexao, id_despesa)
            elif opcao == "3":
                consultar_despesas(conexao)
            elif opcao == "4":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

        fechar_conexao(conexao)

if __name__ == "__main__":
    main()