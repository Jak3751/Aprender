from funcoes import conectar_banco, lancar_despesa, excluir_despesa, consultar_despesas, fechar_conexao

def menu():
    print("==== Sistema de Controle de Despesas ====")
    print("1. Cadastrar tipo Despesa")
    print("2. Lançar Despesa")
    print("3. Excluir Despesa")
    print("4. Consultar Despesas")
    print("5. Sair")

def main():
    conexao = conectar_banco()

    if conexao:
        while True:
            menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "2":
                lancar_despesa(conexao)
            elif opcao == "3":
                id_despesa = int(input("Digite o ID da despesa a ser excluída: "))
                excluir_despesa(conexao, id_despesa)
            elif opcao == "4":
                consultar_despesas(conexao)
            elif opcao == "5":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

        fechar_conexao(conexao)

if __name__ == "__main__":
    main()